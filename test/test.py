import win32gui, win32api, time, random
 
# 获取窗口句柄
# hwnd = 5835322  # 替换为你想要获取坐标的窗口标题
 
def get_mouse_pos_in_window(hwnd):
    # 获取鼠标屏幕坐标
    mouse_pos = win32api.GetCursorPos()

    # 将屏幕坐标转换为窗口坐标
    window_pos = win32gui.ScreenToClient(hwnd, mouse_pos)

    return window_pos

# 获取窗口句柄
hwnd = 4261146

# 获取鼠标在窗口中的坐标
while True:
    print(get_mouse_pos_in_window(hwnd))
    time.sleep(1)



# title = "元梦之星-云游戏-快捷方式 - 元梦之星-腾讯先锋云游戏 - "
# num = "961069561"
# title +=num
# hwnd = win32gui.FindWindowEx(0,0,None,title)
# print(hwnd)
# 从最小化打开窗口
# win32gui.ShowWindow(hwnd,win32con.SW_RESTORE)
# 窗口获取焦点
# win32gui.SetForegroundWindow(hwnd)
# 修改窗口大小
# win32gui.MoveWindow(hwnd,50,50,1000,600,False)
# 获取窗口大小
# rect = win32gui.GetWindowRect(hwnd)
# window_width = rect[2] - rect[0]
# window_height = rect[3] - rect[1]
# print(window_width)
# print(window_height)


# 获取全部句柄和窗口名称
# def _hwnd_(hwnd, mouse):
#     print(f"句柄：{hwnd}\t 名称：{win32gui.GetWindowText(hwnd)}")
# win32gui.EnumWindows(_hwnd_, 0)


# def ck(cx, cy, hwnd, t=0):#后台鼠标点击
#     #后台鼠标点击
#     long_position = win32api.MAKELONG(500, 300)  # 设置位置 坐标
#     win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
#     time.sleep(0.1)
#     win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
#     if t == 0:
#         time.sleep(random.random()*2+1)  # sleep一下
#     else:
#         time.sleep(t)
#     return 0
