import win32gui, win32con,time
 
# 获取当前鼠标位置
def get_mouse_position():
    pt = win32gui.GetCursorPos()
    return pt
 
# 获取特定窗口的客户区鼠标位置
def get_mouse_position_in_window(hwnd):
    pt = win32gui.GetCursorPos()
    win32gui.ScreenToClient(hwnd, pt)
    return pt
 
# 使用示例
# 窗口句柄（这里需要你提供具体的窗口句柄）
hwnd = 789188  # 替换为你的窗口句柄
 
# 获取屏幕上的鼠标位置
screen_pos = get_mouse_position()
print(f"Screen Position: {screen_pos}")
 
# 获取特定窗口的客户区鼠标位置
while True:
    time.sleep(1)
    if hwnd:
        client_pos = get_mouse_position_in_window(hwnd)
        print(f"Client Position in Window {hwnd}: {client_pos}")
    else:
        print("Window handle is not provided.")