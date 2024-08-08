from myTools import *
import threading
import letsgoFarm as lf


def run_letsgoFarm(btn_a, btn_d):
    """开始挂机"""
    btn_active(btn_a)
    btn_disable(btn_d)
    print_log("开始挂机", "green")
    exit_event.clear()
    thread = threading.Thread(target=lambda: lf.start())
    thread.daemon = True
    thread.start()


def threading_fun(fun):
    print_log("请在3秒内点击游戏画面", "green")
    exit_event.clear()

    thread = threading.Thread(target=lambda: fun())
    create_progressbar()
    for _ in range(6):
        exit_event.wait(0.5)
        update_progressbar(50)
    thread.daemon = True
    thread.start()


def fish():
    print_log("请在3秒内点击游戏画面", "green")
    exit_event.clear()
    value = combo.get()
    print_log("选择的是钓鱼{}次".format(value))
    exit_event.clear()
    thread = threading.Thread(target=lambda: lf.fishing(value))
    thread.daemon = True
    thread.start()


# 创建一个窗口并设置窗口的标题
window = create_window("星宝农场自动化")

# 创建一个列表框，第一行
create_listbox()

# 创建一个进度条，第二行
create_progressbar()

# 创建三个个按钮，启动、停止、退出，第四行
btn_run = create_button("运行", 2, 0)
btn_run.config(
    command=lambda: run_letsgoFarm(
        [btn_stop], [btn_run, btn_gotofarm, btn_gotopasture, btn_gotofishpond]
    )
)
btn_stop = create_button("停止", 2, 1)
btn_stop.config(
    command=lambda: stop_letsgoFarm(
        [btn_run, btn_gotofarm, btn_gotopasture, btn_gotofishpond], [btn_stop]
    )
)

btn_quit = create_button("退出", 2, 2)
btn_quit.config(command=window.quit)


# 创建三个按钮，前往农场，前往牧场，前往鱼塘，第三行
btn_gotofarm = create_button("前往农场", 3, 0)
btn_gotofarm.config(command=lambda: threading_fun(lf.go_to_farm))
btn_gotopasture = create_button("前往牧场", 3, 1)
btn_gotopasture.config(command=lambda: threading_fun(lf.go_to_pasture))
btn_gotofishpond = create_button("前往鱼塘", 3, 2)
btn_gotofishpond.config(command=lambda: threading_fun(lf.go_to_fishpond))


# 创建一个Label小部件并添加文本
label = tk.Label(window, text="选择钓鱼次数")
label.grid(row=4, column=0, sticky="nsew")
# 创建下拉列表
combo = ttk.Combobox(window)
combo["values"] = (2, 10, 14, 16, 24)
combo.current(4)  # 设置默认选中第一项
combo.grid(row=4, column=1, sticky="nsew")
# combo.grid_forget()
# 创建钓鱼按钮
btn_fish = create_button("钓鱼", 4, 2)
btn_fish.config(command=lambda: fish())


# 置顶窗口
window.attributes("-topmost", True)
# 设置窗口大小不可改变
window.resizable(False, False)
# 启动事件循环
window.mainloop()
