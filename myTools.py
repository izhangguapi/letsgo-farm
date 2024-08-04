import datetime, time, pyautogui
import tkinter as tk
from tkinter import ttk


def get_datetime():
    """获取当前日期和时间"""
    return str(datetime.datetime.now())


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


# 日志名称
log_name = str(datetime.datetime.now().strftime("%Y年%m月%d日_%H时%M分%S秒"))


def save_log(text):
    """保存日志"""
    # 路径
    path = "log/" + log_name + ".txt"
    with open(path, "a+", encoding="utf-8") as f:
        f.write(text + "\n")


def go_to_farm():
    """走到农场"""
    print_log("等待3秒...", "red")
    create_progressbar()
    for _ in range(3):
        sleep(1)
        update_progressbar(100)
    pyautogui.press("r")
    print_log("开始走到农场...")
    pyautogui.keyDown("a")
    pyautogui.keyDown("w")
    sleep(4.3)
    pyautogui.keyUp("a")
    pyautogui.keyUp("w")
    print_log("到达农场", "green")
    # sleep(1)


def go_to_pasture():
    """走到牧场"""
    print_log("等待3秒...", "red")
    create_progressbar()
    for _ in range(3):
        sleep(1)
        update_progressbar(100)
    pyautogui.press("r")
    print_log("开始走到牧场...")
    pyautogui.keyDown("w")
    sleep(0.8)
    pyautogui.keyDown("d")
    sleep(1.2)
    pyautogui.keyUp("w")
    pyautogui.keyUp("d")
    print_log("到达牧场", "green")
    # sleep(1)


def go_to_fishpond():
    """走到鱼塘，耗时8.9秒"""
    print_log("等待3秒...", "red")
    create_progressbar()
    for _ in range(3):
        sleep(1)
        update_progressbar(100)
    pyautogui.press("r")
    print_log("开始走到鱼塘...")
    pyautogui.keyDown("w")
    pyautogui.keyDown("a")
    sleep(0.5)
    pyautogui.keyUp("a")
    sleep(2.2)
    pyautogui.keyDown("d")
    sleep(0.8)
    pyautogui.keyUp("d")
    sleep(2.4)
    pyautogui.keyUp("w")
    print_log("到达鱼塘", "green")
    # sleep(1)


def create_window(title):
    """创建窗口"""
    global window
    window = tk.Tk()
    window.title(title)
    return window


def create_progressbar():
    """创建进度条"""
    global p
    p = ttk.Progressbar(window, maximum=300, value=0, mode="determinate")
    p.grid(row=1, column=0, columnspan=3, padx=10, sticky="nsew")


def create_button(text, row, column):
    """创建按钮"""
    btn = tk.Button(window, text=text)
    btn.grid(row=row, column=column, pady=(0, 5))
    return btn


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
    lb = tk.Listbox(window, height=5, width=80, font=("Arial", 12))
    lb.grid(row=0, column=0, columnspan=3, sticky="nsew")


def delete_top_item():
    """超过100行就删除顶部的"""
    if len(lb.get(0, tk.END)) > 100:
        lb.delete(0, 0)


def print_log(text, fg="black"):
    """打印日志"""
    log = "[" + get_datetime() + "] - " + text
    try:
        lb.insert(tk.END, log)
        lb.itemconfigure(tk.END, fg=fg)
        lb.see(tk.END)
        save_log(log)
        delete_top_item()
    except:
        print(log)
