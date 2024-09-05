import win32gui, win32api, time, random


def get_mouse_pos_in_window(hwnd):
    # 获取鼠标屏幕坐标
    mouse_pos = win32api.GetCursorPos()

    # 将屏幕坐标转换为窗口坐标
    window_pos = win32gui.ScreenToClient(hwnd, mouse_pos)

    return window_pos


# 获取窗口句柄
hwnd = 5964962

# 获取鼠标在窗口中的坐标
while True:
    print(get_mouse_pos_in_window(hwnd))
    time.sleep(1)
