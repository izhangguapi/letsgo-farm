import pyautogui


# 走到渔场
def go_to_fishery():
    pyautogui.press("r")
    pyautogui.keyDown("a")
    pyautogui.keyDown("w")
    pyautogui.sleep(0.6)
    pyautogui.keyUp("a")
    pyautogui.sleep(6)
    pyautogui.keyUp("w")


# 农场农场
def go_to_farm():
    pyautogui.press("r")
    pyautogui.keyDown("a")
    pyautogui.keyDown("w")
    pyautogui.sleep(4.5)
    pyautogui.keyUp("a")
    pyautogui.keyUp("w")


# 走到牧场
def go_to_pasture():
    pyautogui.press("r")
    pyautogui.keyDown("w")
    pyautogui.sleep(0.7)
    pyautogui.keyDown("d")
    pyautogui.sleep(1.3)
    pyautogui.keyUp("d")
    pyautogui.keyUp("w")
