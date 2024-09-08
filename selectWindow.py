import tkinter as tk
from tkinter import ttk
import myTools, win32gui, win32con


def ok():
    # print(f"句柄：{hwnd}")
    # print(f"标题：{title}")
    try:
        myTools.hwnd = hwnd
        myTools.title = title.replace("元梦之星", "已控制")
        # print(f"句柄：{myTools.hwnd}")
        # print(f"标题：{myTools.title}")
        # 获取窗口的位置和大小
        rect = win32gui.GetWindowRect(myTools.hwnd)
        # 激活窗口
        # win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        # 窗口获取焦点
        # win32gui.SetForegroundWindow(hwnd)
        # 修改窗口大小
        win32gui.MoveWindow(hwnd, rect[0], rect[1], 1000, 600, False)
        # win32gui.SetWindowPos(
        #     hwnd,
        #     win32con.HWND_BOTTOM,
        #     rect[0],
        #     rect[1],
        #     1000,
        #     593,
        #     win32con.SWP_NOACTIVATE,
        # )
        window.destroy()
    except:
        print("请选择窗口后再点击确定")
        pass


def get_hwnd():
    tree.delete(*tree.get_children())

    hwnd = myTools.find_windows_by_title("元梦之星")
    if hwnd:
        for i in hwnd:
            text = win32gui.GetWindowText(i)
            tree.insert("", "end", text=i, values=(text, i))
    else:
        tree.insert("", "end", text="未找到窗口", values=("未找到窗口", "请刷新"))


def on_select(e):
    global hwnd, title
    try:
        item = e.widget.selection()[0]
        title = tree.item(item, "values")[0]
        hwnd = tree.item(item, "values")[1]
    except:
        return


# 创建第一个窗口
def create_window():
    global tree, window, title, hwnd
    window = tk.Toplevel()
    window.title("选择元梦窗口")
    tree = ttk.Treeview(
        window,
        columns=("窗口标题", "句柄"),
        show="headings",
        selectmode="browse",
    )
    tree.heading("窗口标题", text="窗口标题")
    tree.heading("句柄", text="句柄")
    tree.column("窗口标题", width=200)
    tree.column("句柄", width=100)
    tree.bind("<<TreeviewSelect>>", on_select)
    tree.grid(row=0, column=0, columnspan=2, sticky="nsew")

    btn_refresh = tk.Button(window, text="刷新", command=get_hwnd)
    btn_refresh.grid(row=1, column=0, pady=5)
    btn_ok = tk.Button(window, text="确定", command=ok)
    btn_ok.grid(row=1, column=1, pady=5)

    title, hwnd = None, None

    get_hwnd()
    window.resizable(False, False)
    window.grab_set()
