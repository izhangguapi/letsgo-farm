import pyautogui, os

os.system("open -a '元梦之星-云游戏-快捷方式'")
pyautogui.sleep(1)
def screenshot():
    img_path = "images/fishery.png"
    location = pyautogui.locateOnScreen(img_path, confidence=0.8)

    # 苹果系统专用，没有次行代码会导致截图位置错误，Windows未测试，如果出现截图不正确请注释下一行
    location = (location[0] // 2, location[1] // 2, location[2] // 2, location[3] // 2)

    imag = pyautogui.screenshot(region=location)

    imag.save("images/temp/now_farm.png")  # 保存位置
    imag.show()  # 显示位置
