import ctypes
import win32gui
import win32ui
import win32con
import win32api
from PIL import Image

def screenshot_window(hwnd):
    # 获取窗口大小
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    print("Window size: {}x{}".format(width, height))

    # 创建设备上下文
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    # 创建位图对象
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    # 使用 ctypes 调用 PrintWindow
    result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    # result = saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    # 如果 PrintWindow 成功，则保存位图
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    # 清理资源
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:  # PrintWindow 成功
        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
        im.show()
        print("Screenshot saved as screenshot.png")
    else:
        print("Failed to capture window.")

# 查找窗口句柄
# hwnd = win32gui.FindWindow(None, "LocalSend")
hwnd = 7866038
# hwnd = 4719734
if hwnd:
    screenshot_window(hwnd)
else:
    print("Window not found.")