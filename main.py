from myTools import *
import threading
import letsgoFarm


def run_letsgoFarm():
    """启动多线程程序"""
    btn_run.config(state="disabled")
    btn_gotofarm.config(state="disabled")
    btn_gotopasture.config(state="disabled")
    btn_gotofishpond.config(state="disabled")
    print_log("启动多线程", "green")
    thread = threading.Thread(target=lambda: letsgoFarm.start())
    thread.daemon = True
    thread.start()


def btn_farm():
    print_log("请在3秒内点击游戏画面", "green")
    thread = threading.Thread(target=lambda: go_to_farm())
    thread.daemon = True
    thread.start()


def btn_pasture():
    print_log("请在3秒内点击游戏画面", "green")
    thread = threading.Thread(target=lambda: go_to_pasture())
    thread.daemon = True
    thread.start()


def btn_fishpond():
    print_log("请在3秒内点击游戏画面", "green")
    thread = threading.Thread(target=lambda: go_to_fishpond())
    thread.daemon = True
    thread.start()


# 创建一个窗口并设置窗口的标题
window = create_window("星宝农场自动化")

# 创建一个列表框，第一行
create_listbox()

# 创建一个进度条，第二行
create_progressbar()

# 创建三个按钮，前往农场，前往牧场，前往鱼塘，第三行
btn_gotofarm = create_button("前往农场", 2, 0)
btn_gotofarm.config(command=lambda: btn_farm())
btn_gotopasture = create_button("前往牧场", 2, 1)
btn_gotopasture.config(command=lambda: btn_pasture())
btn_gotofishpond = create_button("前往鱼塘", 2, 2)
btn_gotofishpond.config(command=lambda: btn_fishpond())

# 创建两个按钮，启动和退出，第四行
btn_run = create_button("开始挂机", 3, 0)
btn_run.config(command=lambda: run_letsgoFarm())
btn_quit = create_button("退出", 3, 1)
btn_quit.config(command=window.quit)


# 置顶窗口
window.attributes("-topmost", True)
# 设置窗口大小不可改变
window.resizable(False, False)
# 启动事件循环
window.mainloop()
