import datetime, time, pyautogui


class ANSI:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[m"


def get_date():
    """获取当前日期和时间"""
    return "[" + str(datetime.datetime.now()) + "] - "


def print_red(text):
    """打印红色文本"""
    print(ANSI.RED + get_date() + text + ANSI.RESET)


def print_green(text):
    """打印绿色文本"""
    print(ANSI.GREEN + get_date() + text + ANSI.RESET)


def print_nol(text):
    print(get_date() + text)


def sleep(seconds):
    """休眠的异常处理"""
    try:
        time.sleep(seconds)
    except:
        print_red("程序被强制退出")
        exit()


# 走到渔场
def go_to_fishpond():
    pyautogui.press("r")
    pyautogui.keyDown("a")
    pyautogui.keyDown("w")
    sleep(0.6)
    pyautogui.keyUp("a")
    sleep(6)
    pyautogui.keyUp("w")
    # sleep(1)


# 农场农场
def go_to_farm():
    pyautogui.press("r")
    pyautogui.keyDown("a")
    pyautogui.keyDown("w")
    sleep(4.5)
    pyautogui.keyUp("a")
    pyautogui.keyUp("w")
    # sleep(1)


# 走到牧场
def go_to_pasture():
    pyautogui.press("r")
    pyautogui.keyDown("w")
    sleep(0.7)
    pyautogui.keyDown("d")
    sleep(1.3)
    pyautogui.keyUp("d")
    pyautogui.keyUp("w")
    # sleep(1)
