import tkinter as tk
import pyautogui
import random
import threading

# 初始化全局变量
running = False

# 鼠标移动函数
def move_mouse():
    while running:
        # 随机生成屏幕上的位置
        x = random.randint(0, pyautogui.size().width - 1)
        y = random.randint(0, pyautogui.size().height - 1)
        # 移动鼠标到新位置
        pyautogui.moveTo(x, y, duration=0.5)
        # 等待30秒
        threading.Event().wait(30)

# 开始按钮功能
def start():
    global running
    if not running:  # 防止重复启动线程
        running = True
        threading.Thread(target=move_mouse, daemon=True).start()

# 结束按钮功能
def end():
    global running
    running = False

# 创建主窗口
root = tk.Tk()
root.title("鼠标移动控制")
root.geometry("300x200")

# 创建按钮
start_button = tk.Button(root, text="Start", font=("Arial", 14), command=start)
start_button.pack(pady=20)

end_button = tk.Button(root, text="End", font=("Arial", 14), command=end)
end_button.pack(pady=20)

# 运行主循环
root.mainloop()
