import pyautogui as pg


class ANSI:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[m"


def print_red(text):
    """打印红色文本"""
    print(ANSI.RED + text + ANSI.RESET)


def print_green(text):
    """打印绿色文本"""
    print(ANSI.GREEN + text + ANSI.RESET)


def get_date():
    return pg.time.strftime("%Y年%m届%d日 %H:%M:%S - ", pg.time.localtime())


def open_game():
    """打开元梦并解除省电模式，耗时3秒"""
    print(get_date() + "寻找并打开游戏")
    # 设置游戏图标的坐标并移到改坐标，然后点击
    x, y = 1000, 1125
    pg.moveTo(x, y, duration=1)
    pg.click()
    pg.sleep(1)

    # 点击屏幕中间解除省电模式
    x, y = 900, 585
    # print("解除省电模式")
    pg.click(x, y)
    pg.sleep(1)


def farm():
    """收获农场，耗时1秒"""
    # print("收获农场")
    # x, y = 1360, 715
    # pg.click(x, y)
    print(get_date() + "收获农场中...")
    pg.press("q")
    pg.sleep(1)


def pasture():
    """收获牧场，耗时1秒"""
    # x, y = 1540, 640
    # pg.click(x, y)
    print(get_date() + "收获牧场")
    pg.press("e")
    pg.sleep(1)


def find_drones():
    """寻找无人机，耗时1秒"""
    # 重置位置后，按下a键一秒钟
    print(get_date() + "寻找无人机...")
    pg.press("r")
    pg.keyDown("a")
    pg.sleep(1)
    pg.keyUp("a")


def open_browser():
    '''打开浏览器，耗时2秒'''
    # print("打开浏览器")
    print(get_date() + "打开浏览器")
    x, y = 600, 1125
    pg.click(x, y)
    pg.sleep(1)
    pg.moveTo(1770, 675, duration=1)
    pg.click()


def start():
    print_red(get_date() + "开始执行")
    num = 1
    while True:
        print_green(get_date() + "第{}次执行".format(num))
        if num % 11 == 0:
            print_red(get_date() + "收获{}次".format(num // 11))
        num += 1
        open_game()
        find_drones()
        farm()
        open_browser()
        # 休息两分钟
        print(get_date() + "休息2分钟...")
        pg.sleep(120)
        open_game()
        find_drones()
        pasture()
        open_browser()
        # 休息三分钟左右（时间根据实际情况调整，尽量控制浇水后时间减少的是一分钟）
        print(get_date() + "休息2分钟...")
        pg.sleep(115)


if __name__ == "__main__":
    # 执行任务
    start()
