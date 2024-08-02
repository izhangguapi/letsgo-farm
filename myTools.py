import datetime, time, pyautogui
import tkinter as tk
from tkinter import ttk

# 已弃用
# class ANSI:
#     RED = "\033[31m"
#     GREEN = "\033[32m"
#     RESET = "\033[m"
# def print_red(text):
#     """打印红色文本"""
#     print(ANSI.RED + get_date() + text + ANSI.RESET)
# def print_green(text):
#     """打印绿色文本"""
#     print(ANSI.GREEN + get_date() + text + ANSI.RESET)
# def print_nol(text):
#     print(get_date() + text)


def get_datetime():
    """获取当前日期和时间"""
    return str(datetime.datetime.now())


# def get_date():
#     """获取当前日期"""
#     return str(datetime.date.today())


def sleep(seconds):
    """休眠的异常处理"""
    if seconds < 0:
        print_log("休眠时间小于0，跳过", "red")
        return
    try:
        time.sleep(seconds)
    except:
        print_log("程序被强制退出", "red")
        exit()


def create_window(title):
    """创建窗口"""
    global window
    window = tk.Tk()
    window.title(title)
    return window


def create_progressbar():
    """创建进度条"""
    global p
    p = ttk.Progressbar(window, length=200, value=0, mode="determinate")
    p.grid(row=1, column=0, columnspan=2, padx=10, sticky="nsew")


def update_progressbar(num):
    """更新进度条"""
    p["value"] = p["value"] + num
    window.update()


def clear_progressbar():
    """清除进度条"""
    p["value"] = 0
    window.update()


def create_listbox():
    """创建列表框"""
    global lb
    lb = tk.Listbox(window, height=5, width=60, font=("Arial", 12))
    lb.grid(row=0, column=0, columnspan=2, sticky="nsew")


def delete_top_item():
    """超过100行就删除顶部的"""
    if len(lb.get(0, tk.END)) > 100:
        lb.delete(0, 0)


def print_log(text, fg="black"):
    """打印日志"""

    log = "[" + get_datetime() + "] - " + text
    lb.insert(tk.END, log)
    lb.itemconfigure(tk.END, fg=fg)
    lb.see(tk.END)
    save_log(log)
    delete_top_item()


log_name = get_datetime()


def save_log(text):
    """保存日志"""
    # 路径
    path = "log/" + log_name + ".txt"
    with open(path, "a+", encoding="utf-8") as f:
        f.write(text + "\n")


def go_to_fishpond():
    """走到鱼塘"""
    pyautogui.press("r")
    print_log("正在走到鱼塘...")
    pyautogui.keyDown("w")
    pyautogui.keyDown("a")
    sleep(0.3)
    pyautogui.keyUp("a")
    sleep(3)
    pyautogui.keyDown("d")
    sleep(0.5)
    pyautogui.keyUp("d")
    sleep(1.8)
    pyautogui.keyUp("w")
    # sleep(1)


def go_to_farm():
    """走到农场"""
    pyautogui.press("r")
    print_log("正在走到农场...")
    pyautogui.keyDown("a")
    pyautogui.keyDown("w")
    sleep(4.5)
    pyautogui.keyUp("a")
    pyautogui.keyUp("w")
    # sleep(1)


def go_to_pasture():
    """走到牧场"""
    pyautogui.press("r")
    print_log("正在走到牧场...")
    pyautogui.keyDown("w")
    sleep(0.7)
    pyautogui.keyDown("d")
    sleep(1.3)
    pyautogui.keyUp("d")
    pyautogui.keyUp("w")
    # sleep(1)
