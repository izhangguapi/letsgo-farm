import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"鼠标当前位置: x={x}, y={y}")
    pyautogui.sleep(1)