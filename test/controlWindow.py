import time
import win32api
import win32gui
import win32con


class VirtualKeyboard:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.hwnd_title = win32gui.GetWindowText(hwnd)

    # 模拟一次按键的输入，间隔值默认0.1S
    def key_press(self, key: str, interval=0.1):
        key = ord(key.upper())
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
        time.sleep(interval)
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
    def mouse_move(self, x, y):
        x = int(x)
        y = int(y)
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, None, point)

    # 模拟鼠标的按键抬起
    def mouse_up(self, x, y, button="L"):
        x = int(x)
        y = int(y)
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
    def mouse_down(self, x, y, button="L"):
        x = int(x)
        y = int(y)
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
    def mouse_double(self, x, y):
        x = int(x)
        y = int(y)
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, point
        )
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
        )

    # 模拟鼠标移动到坐标，并进行左键单击
    def mouse_move_press(self, x, y):
        x = int(x)
        y = int(y)
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, None, point)
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, point
        )
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
        )

    # 模拟鼠标移动到坐标，并进行左键双击
    def mouse_move_press_double(self, x, y):
        x = int(x)
        y = int(y)
        point = win32api.MAKELONG(x, y)
        win32api.PostMessage(self.hwnd, win32con.WM_MOUSEMOVE, None, point)
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONDBLCLK, win32con.MK_LBUTTON, point
        )
        win32api.PostMessage(
            self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, point
        )


if __name__ == "__main__":
    # 1.根据窗口标题获取句柄，通过标题查找，仅返回一个顶层窗口的句柄，不支持模糊查询
    try:
        # 获取窗口句柄
        handle = win32gui.FindWindow(
            None, "元梦之星-云游戏-快捷方式 - 元梦之星-腾讯先锋云游戏 - 208038018"
        )  # 通过窗口标题获取窗口句柄
        # handle = 10095228
        print("窗口句柄是：{}".format(handle))
        vkb = VirtualKeyboard(handle)
        # vkb.mouse_move(100,100)
        # vkb.mouse_move_press(50, 50)
        vkb.key_press("r")
        vkb.key_press("a", 1)
        vkb.key_press("w", 3)
    except Exception as e:
        print("窗口句柄获取失败：{}".format(e))
