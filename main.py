from walk import *
from myTools import *
from identify import *


# 已弃用
# def open_game():
#     """打开元梦并解除省电模式，耗时3秒"""
#     print(get_date() + "寻找并打开游戏")
#     # 设置游戏图标的坐标并移到改坐标，然后点击
#     x, y = 1000, 1125
#     pyautogui.moveTo(x, y, duration=1)
#     pyautogui.click()
#     sleep(1)
#     # 点击屏幕中间解除省电模式
#     x, y = 900, 585
#     # print("解除省电模式")
#     pyautogui.click(x, y)
#     sleep(1)

# 已弃用
# def open_browser():
#     '''打开浏览器，耗时2秒'''
#     # print("打开浏览器")
#     print(get_date() + "打开浏览器")
#     x, y = 600, 1125
#     pyautogui.click(x, y)
#     sleep(1)
#     pyautogui.moveTo(1770, 675, duration=1)
#     pyautogui.click()


def open_ymzx():
    """打开元梦"""
    os.system("open -a '元梦之星-云游戏-快捷方式'")
    print_nol("打开元梦")
    sleep(1)
    pyautogui.press("r", presses=2, interval=0.5)


def open_browser():
    """打开抖音"""
    os.system("open -a 'Google Chrome'")
    print_nol("打开浏览器刷抖音")
    sleep(1)
    pyautogui.press("down")
    sleep(1)
    pyautogui.press("up")


def farm():
    """无人机前往农场"""
    # print("收获农场")
    # x, y = 1360, 715
    # pyautogui.click(x, y)
    print_nol("无人机前往牧场农场")
    pyautogui.press("Q")


def pasture():
    """无人机前往牧场"""
    # x, y = 1540, 640
    # pyautogui.click(x, y)
    print_nol("无人机前往牧场")
    pyautogui.press("E")


def fishery():
    """收获渔场"""
    print_nol("走到渔场")
    go_to_fishery()
    try:
        print_nol("识别是否能够钓鱼")
        identify_img("fishing", 0.8)
    except:
        print_red("不能钓鱼，检测还剩多少时间成熟")
        try:
            screenshot_save("fishery")
            time = OCR_time("fishery")
            if time < 210:
                t = time - 7
                specific_time = datetime.datetime.now() + datetime.timedelta(seconds=t)
                print_nol("等待{}秒后开始钓鱼具体时间为{}".format(t, specific_time))
                sleep(t)
                go_to_fishery()
            else:
                print_red("等待时间超过3分半，跳过")
                return
        except:
            print_red("识别失败，可能未洒饵，按下空格洒饵")
            pyautogui.press("space")
            return

    for _ in range(2):
        print_green("开始钓鱼")
        pyautogui.press("space")

        for j in range(5):
            sleep(0.5)
            try:
                identify_img("fishing_ok", 0.8)
                print_green("上鱼了，开始抬竿")
                pyautogui.press("space")
                break
            except:
                print_red("还没上鱼，还不能抬竿")
                if j == 4:
                    print_red("等待超时，自动抬竿")
                    pyautogui.press("space")
                    break

        print_nol("等待6秒")
        pyautogui.sleep(6)
        print_nol("连按空格")
        pyautogui.press("space", presses=6, interval=0.5)

    # 检测是否钓鱼完成，可以撒饵
    print_nol("检测钓鱼是否完成")
    try:
        identify_img("fishing", 0.8)
        print_nol("洒饵")
        pyautogui.press("space")
        print_nol("钓鱼结束")
    except:
        print_green("已经洒饵，钓鱼结束")


def find_drones():
    """寻找无人机"""
    # 重置位置后，按下a键一秒钟
    pyautogui.press("r")
    print_nol("寻找无人机")
    pyautogui.keyDown("a")
    sleep(1)
    pyautogui.keyUp("a")


def start():
    print_red("开始执行")
    # num = 1
    while True:
        # print_green("第{}次执行".format(num))

        # # 检测农场
        # timestamp_start = time.time()
        # open_ymzx()
        # find_drones()
        # farm()
        # # 检测渔场
        # fishery()
        # open_browser()
        # # 计算耗时
        # timestamp_end = time.time()
        # computation_time = round(timestamp_end - timestamp_start, 2)
        # print_nol("收获农场和渔场耗时：{}秒".format(computation_time))
        # print_green("休息{}秒...".format(120 - computation_time))
        # sleep(120 - computation_time)

        # 检测牧场
        timestamp_start = datetime.datetime.now()
        # open_ymzx()
        find_drones()
        pasture()
        # 检测渔场
        fishery()
        # open_browser()
        # 计算耗时
        timestamp_end = datetime.datetime.now()
        computation_time = timestamp_end - timestamp_start
        # computation_time = round(timestamp_end - timestamp_start, 2)
        t = 300 - computation_time.total_seconds()
        print_nol(
            "收获农场和渔场耗时：{}秒".format(
                round((computation_time).total_seconds(), 2)
            )
        )
        print_green(
            "休息{}秒，下次运行时间：{}".format(
                t, timestamp_end + datetime.timedelta(seconds=t)
            )
        )
        sleep(t)

        # 判断是否执行了11次的倍数
        # if num % 11 == 0:
        #     print_red("大概收获{}波".format(num // 11))
        # num += 1


if __name__ == "__main__":
    # 执行任务
    open_ymzx()
    start()
