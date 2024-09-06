import ctypes
import ctypes.wintypes
import win32gui
import win32con
import time
from PIL import Image

user32 = ctypes.windll.user32

# 定义相关类型
HWND = ctypes.wintypes.HWND
HDC = ctypes.wintypes.HDC
HBITMAP = ctypes.wintypes.HBITMAP

# 定义 PrintWindow 函数的参数类型
PrintWindow = user32.PrintWindow
PrintWindow.argtypes = [HWND, HDC, ctypes.wintypes.UINT]
PrintWindow.restype = ctypes.wintypes.BOOL

def capture_window(hwnd):
    # 获取窗口大小
    rect = ctypes.wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    # 创建设备上下文
    hdc_window = user32.GetWindowDC(hwnd)
    hdc_mem = user32.CreateCompatibleDC(hdc_window)

    # 创建位图
    hbitmap = user32.CreateCompatibleBitmap(hdc_window, width, height)
    user32.SelectObject(hdc_mem, hbitmap)

    # 调用 PrintWindow 进行截图
    result = PrintWindow(hwnd, hdc_mem, 0)

    # 保存位图到文件
    bmpinfo = ctypes.wintypes.BITMAPINFO()
    bmpinfo.bmiHeader.biSize = ctypes.sizeof(ctypes.wintypes.BITMAPINFOHEADER)
    bmpinfo.bmiHeader.biWidth = width
    bmpinfo.bmiHeader.biHeight = -height  # 负数表示从上到下
    bmpinfo.bmiHeader.biPlanes = 1
    bmpinfo.bmiHeader.biBitCount = 32
    bmpinfo.bmiHeader.biCompression = win32con.BI_RGB

    bitmap_data = ctypes.create_string_buffer(width * height * 4)
    user32.GetDIBits(hdc_mem, hbitmap, 0, height, bitmap_data, bmpinfo, win32con.DIB_RGB_COLORS)

    # 释放资源
    user32.DeleteObject(hbitmap)
    user32.DeleteDC(hdc_mem)
    user32.ReleaseDC(hwnd, hdc_window)

    # 将数据转换为图像
    image = Image.frombuffer('RGBA', (width, height), bitmap_data.raw, 'raw', 'BGRA', 0, 1)
    image.save('captured_window.png')

    if result:
        print("截图成功，已保存为 captured_window.png")
    else:
        print("截图失败")

# 获取要截图的窗口句柄（这里假设是记事本窗口）
hwnd = 4524054
if hwnd:
    capture_window(hwnd)
else:
    print("未找到指定窗口")