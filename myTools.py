import datetime, pyautogui, threading
import tkinter as tk
from tkinter import ttk


def get_datetime():
    """获取当前日期和时间"""
    return str(datetime.datetime.now())


exit_event = threading.Event()


def stop_letsgoFarm(btn_a, btn_d):
    """停止程序"""
    exit_event.set()
    btn_disable(btn_d)
    btn_active(btn_a)


def sleep(s):
    """休眠的异常处理"""
    if exit_event.is_set():
        print_log("停止挂机", "red")
        exit()
    elif s < 0:
        print_log("休眠时间小于0，跳过", "red")
        return
    else:
        exit_event.wait(s)


# 日志名称
log_name = str(datetime.datetime.now().strftime("%Y年%m月%d日_%H时%M分%S秒"))


def save_log(text):
    """保存日志"""
    # 路径
    path = "log/" + log_name + ".txt"
    with open(path, "a+", encoding="utf-8") as f:
        f.write(text + "\n")




def create_window(title):
    """创建窗口"""
    global window
    window = tk.Tk()
    window.title(title)
    return window


def create_listbox():
    """创建列表框"""
    global lb
    lb = tk.Listbox(window, height=5, width=80, font=("Arial", 12))
    lb.grid(row=0, column=0, columnspan=4, sticky="nsew")


def create_progressbar():
    """创建进度条"""
    global p
    p = ttk.Progressbar(window, maximum=300, value=0, mode="determinate")
    p.grid(row=1, column=0, columnspan=4, padx=10, sticky="nsew")


def create_button(text, row, column):
    """创建按钮"""
    btn = tk.Button(window, text=text)
    btn.grid(row=row, column=column, pady=(0, 5))
    return btn


def btn_active(btn_list):
    for btn in btn_list:
        btn.config(state="active")


def btn_disable(btn_list):
    for btn in btn_list:
        btn.config(state="disabled")


def update_progressbar(num):
    """更新进度条"""
    p["value"] = p["value"] + num
    window.update()


def clear_progressbar():
    """清除进度条"""
    p["value"] = 0
    window.update()


def delete_top_item():
    """超过100行就删除顶部的"""
    if len(lb.get(0, tk.END)) > 100:
        lb.delete(0, 0)


def print_log(text, fg="black"):
    """打印日志"""
    log = "[" + get_datetime() + "] - " + str(text)
    try:
        lb.insert(tk.END, log)
        lb.itemconfigure(tk.END, fg=fg)
        lb.see(tk.END)
        save_log(log)
        delete_top_item()
    except:
        print(log)
