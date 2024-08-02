from myTools import *
import threading
import letsgoFarm


def run_program():
    """启动多线程程序"""
    button_run.config(state="disabled")
    print_log("启动", "green")
    thread = threading.Thread(target=lambda: letsgoFarm.start())
    thread.daemon = True
    thread.start()


# 创建一个窗口并设置窗口的标题
window = create_window("星宝农场自动化")
# window = tk.Tk()
# window.title()
# 创建一个列表框
create_listbox()
# listbox = tk.Listbox(window, height=5, width=80, font=("Arial", 12))
# listbox.grid(row=0, column=0, columnspan=2, sticky="nsew")

create_progressbar()

# 创建两个按钮，启动和退出
button_run = tk.Button(
    window, text="启动", fg="green", state="active", command=lambda: run_program()
)
button_run.grid(row=2, column=0, pady=(0, 5))
button_quit = tk.Button(window, text="退出", fg="red", command=window.quit)
button_quit.grid(row=2, column=1, pady=(0, 5))

# button = tk.Button(window, text="增加", command=lambda: update_progressbar(1))
# button.grid(row=3, column=1, pady=(0, 5))

# 置顶窗口
window.attributes("-topmost", True)
# 设置窗口大小不可改变
window.resizable(False, False)
# 启动事件循环
window.mainloop()
