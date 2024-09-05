import datetime, threading, win32gui, win32api, win32con, win32ui, json, os, ctypes
from paddleocr import PaddleOCR
from PIL import Image
import tkinter as tk

hwnd = None
title = None
exit_event = threading.Event()
lgf_config = {
    "farm_enable": True,
    "farm_timer": False,
    "farm_time": "",
    "pasture_enable": True,
    "pasture_timer": False,
    "pasture_time": "",
    "fishpond_enable": True,
    "fishpond_timer": False,
    "fishpond_time": "",
    "loop_s": 530,
    "prayers_enable": False,
    "prayers_time": "",
    "prayers_uid": [],
}


class CalculationWaiting:
    """计算等待时间"""

    def __init__(self, seconds=530):
        self.time = seconds
        self.start_time = None
        self.end_time = None

    def set_now(self):
        self.start_time = datetime.datetime.now()

    def computing_time(self):
        self.end_time = datetime.datetime.now()
        time_difference = (self.end_time - self.start_time).total_seconds()
        s = lgf_config["loop_s"] - time_difference
        specific_time = self.computing_specific_time(time=self.end_time, seconds=s)
        print_log(f"本次任务耗时: {time_difference} 秒，休息 {s} 秒", "green")
        print_log(f"下次运行时间: {specific_time}", "green")
        sleep(s)

    def computing_specific_time(self, seconds, time=datetime.datetime.now()):
        return time + datetime.timedelta(seconds=seconds)


class WindowController:

    def __init__(self, hwnd):
        self.hwnd = hwnd

    # 模拟一次按键的输入，间隔值默认0秒
    def key_press(self, key: str, interval=0.1):
        key = ord(key.upper())
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
        sleep(interval)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, key, 0)

    # 模拟一个按键的按下
    def key_down(self, key: str):
        key = ord(key.upper())
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)

    # 模拟一个按键的弹起
    def key_up(self, key: str):
        key = ord(key.upper())
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, key, 0)

    # 模拟鼠标的移动
    def mouse_move(self, position):
        x, y = position
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, None, point)

    # 模拟鼠标的按键抬起
    def mouse_up(self, position, button="L"):
        x, y = position
        button = button.upper()
        point = win32api.MAKELONG(x, y)
        if button == "L":
            win32api.PostMessage(
                self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
            )
        elif button == "R":
            win32api.PostMessage(
                self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, point
            )

    # 模拟鼠标的按键按下
    def mouse_down(self, position, button="L"):
        x, y = position
        button = button.lower()
        point = win32api.MAKELONG(x, y)
        if button == "L":
            win32api.PostMessage(
                self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, point
            )
        elif button == "R":
            win32api.PostMessage(
                self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, point
            )

    # 模拟鼠标的左键双击
    def mouse_double(self, position):
        x, y = position
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, point
        )
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
        )

    # 模拟鼠标移动到坐标，并进行左键单击
    def mouse_move_press(self, position):
        x, y = position
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, None, point)
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, point
        )
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
        )

    # 模拟鼠标移动到坐标，并进行左键双击
    def mouse_move_press_double(self, position):
        x, y = position
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, None, point)
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, point
        )
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
        )

    # 截取窗口
    def screenshot_window(self, position=None):
        x = 0
        y = 0
        width = 0
        height = 0
        if position:
            x, y, width, height = position
        else:
            l, t, r, b = win32gui.GetWindowRect(self.hwnd)
            width = r - l
            height = b - t

        # 获取窗口的设备上下文（DC）
        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        # 创建一个空的位图对象
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
        saveDC.SelectObject(saveBitMap)

        # 将窗口内容拷贝到位图对象中
        # result = win32gui.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
        # result = ctypes.windll.user32.PrintWindow(self.hwnd, saveDC.GetSafeHdc(), 0)
        saveDC.BitBlt((0, 0), (width, height), mfcDC, (x, y), win32con.SRCCOPY)
        # print("截图结果：", result)
        
        # 从位图对象中保存图像
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        # 释放资源
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwndDC)

        # if result == 1:
        img = Image.frombuffer(
            "RGB",
            (bmpinfo["bmWidth"], bmpinfo["bmHeight"]),
            bmpstr,
            "raw",
            "BGRX",
            0,
            1,
        )
        # img.show()
        img_path = os.path.join(
            os.environ.get("TEMP"), get_datetime().replace(":", "_") + ".png"
        )
        img.save(img_path)
        return img_path


def get_datetime():
    """获取当前日期和时间"""
    return str(datetime.datetime.now())


def get_position():
    position = None
    with open("position.json", "r", encoding="utf-8") as file:
        position = json.load(file)
    return position


def get_key():
    key = None
    with open("key.json", "r", encoding="utf-8") as file:
        key = json.load(file)
    return key


def ocr_img(img_path):
    """
    识别图片中的时间，并将其转为秒
    参数:
    img(str): 图片名称,会自动添加

    返回值: 返回图片中时间转为秒，以及图片识别耗时
    """
    # 创建一个PaddleOCR对象
    ocr = PaddleOCR(show_log=False, lang="ch", use_angle_cls=False)
    # 使用PaddleOCR对象进行图片识别
    result = ocr.ocr(img_path, cls=False)
    print_log("识别结果：{}".format(result))
    result = result[0]
    list_text = []
    if result:
        for i in result:
            list_text.append(i[1][0])
    os.remove(img_path)
    return list_text


def sleep(s):
    """休眠的异常处理"""
    if s < 0:
        print_log("休眠时间小于0，跳过", "red")
        return
    elif not exit_event.is_set():
        exit_event.wait(s)
    else:
        print_log("停止挂机")
        exit()


def check_settings(name):
    enable = lgf_config[name + "_enable"]
    timer = lgf_config[name + "_timer"]
    if not enable:
        return False
    if enable and not timer:
        return True
    time = lgf_config[name + "_time"]
    now = datetime.datetime.now()
    print_log("当前时间：", now)
    print_log("设定时间：", time)
    farm_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    if now < farm_time:
        return True
    else:
        print_log("超过设定时间，不予执行")
        return False


def convert_to_seconds(time):
    if "后" in time:
        time = time.split("后")[0]
        h, s, m = 0, 0, 0
        if "时" in time:
            temp = time.split("小时")
            h = int(temp[0])
            time = temp[1]
        if "分" in time:
            temp = time.split("分")
            m = int(temp[0])
            time = temp[1]
        if "秒" in time:
            s = int(time.split("秒")[0])
        seconds = h * 3600 + m * 60 + s
        print_log(f"转为秒：{seconds}")
        return seconds
    else:
        return None


# def create_window(title):
#     """创建窗口"""
#     global window
#     window = tk.Tk()
#     window.title(title)
#     return window


# def create_progressbar():
#     """创建进度条"""
#     global p
#     p = ttk.Progressbar(window, maximum=300, value=0, mode="determinate")
#     p.grid(row=1, column=0, columnspan=4, padx=10, sticky="nsew")


# def create_button(text, row, column):
#     """创建按钮"""
#     btn = tk.Button(window, text=text)
#     btn.grid(row=row, column=column, pady=(0, 5))
#     return btn


# def btn_active(btn_list):
#     for btn in btn_list:
#         btn.config(state="active")


# def btn_disable(btn_list):
#     for btn in btn_list:
#         btn.config(state="disabled")


# def update_progressbar(num):
#     """更新进度条"""
#     p["value"] = p["value"] + num
#     window.update()


# def clear_progressbar():
#     """清除进度条"""
#     p["value"] = 0
#     window.update()


def create_listbox(window: tk.Tk):
    """创建列表框"""
    global lb
    lb = tk.Listbox(window, height=5, font=("Arial", 10))
    lb.grid(row=2, column=0, columnspan=5, sticky="nsew")


def delete_top_item():
    """超过100行就删除顶部的"""
    if len(lb.get(0, tk.END)) > 100:
        lb.delete(0, 0)


# 日志名称
log_name = None
current_path = os.path.dirname(os.path.abspath(__file__))


def save_log(text):
    """保存日志"""
    # 路径
    path = os.path.join(current_path, "log", log_name)
    with open(path, "a+", encoding="utf-8") as f:
        f.write(text + "\n")


def print_log(text, fg="black"):
    """打印日志"""
    log = "[" + get_datetime() + "] - " + str(text)
    try:
        lb.insert(tk.END, log)
        lb.itemconfigure(tk.END, fg=fg)
        lb.see(tk.END)
        delete_top_item()
    except:
        print(log)
    save_log(log)


# 获取全部窗口句柄
def get_all_windows():
    windows = []

    def callback(hwnd, windows):
        windows.append(hwnd)

    win32gui.EnumWindows(callback, windows)
    return windows


# 根据标题寻找窗口
def find_windows_by_title(title):
    windows = get_all_windows()
    result = []
    for hwnd in windows:
        if title in win32gui.GetWindowText(hwnd):
            result.append(hwnd)
    return result
