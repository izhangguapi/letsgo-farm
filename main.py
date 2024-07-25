import os, time
from walk import *
from myTools import *
from identify import *
import pyautogui as pg


# 已弃用
# def open_game():
#     """打开元梦并解除省电模式，耗时3秒"""
#     print(get_date() + "寻找并打开游戏")
#     # 设置游戏图标的坐标并移到改坐标，然后点击
#     x, y = 1000, 1125
#     pg.moveTo(x, y, duration=1)
#     pg.click()
#     sleep(1)
#     # 点击屏幕中间解除省电模式
#     x, y = 900, 585
#     # print("解除省电模式")
#     pg.click(x, y)
#     sleep(1)

# 已弃用
# def open_browser():
#     '''打开浏览器，耗时2秒'''
#     # print("打开浏览器")
#     print(get_date() + "打开浏览器")
#     x, y = 600, 1125
#     pg.click(x, y)
#     sleep(1)
#     pg.moveTo(1770, 675, duration=1)
#     pg.click()


def open_ymzx():
    """打开元梦"""
    os.system("open -a '元梦之星-云游戏-快捷方式'")
    print_nol("打开元梦")
    sleep(1)


def open_browser():
    """打开抖音"""
    os.system("open -a 'Google Chrome'")
    print_nol("打开浏览器")
    sleep(1)
    pg.press("down")
    sleep(1)
    pg.press("up")


def farm():
    """收获农场"""
    # print("收获农场")
    # x, y = 1360, 715
    # pg.click(x, y)
    print_nol("收获农场中...")
    pg.press("Q")



def pasture():
    """收获牧场"""
    # x, y = 1540, 640
    # pg.click(x, y)
    print_nol("收获牧场中...")
    pg.press("E")



def fishery():
    """收获渔场"""
    print_nol("走到渔场")
    go_to_fishery()

    try:
        print_nol("识别是否能够钓鱼")
        screenshot("harvest_fish")
    except:
        print_red("不能钓鱼，检测还剩多少时间成熟")
        try:
            screenshot("fishery")
            time, spend = OCR_time("fishery")
            if time < 60:
                print_nol("等待{}秒后开始钓鱼".format(time - spend))
                sleep(time - spend)
            else:
                print_red("等待时间超过1分钟，跳过")
                return
        except:
            print_red("识别失败，可能未洒饵，按下空格")
            pg.press("space")
            return

    for i in range(2):
        img_path = "images/fishing.png"
        try:
            print_nol("开始寻找钓鱼按钮")
            pg.locateOnScreen(img_path, confidence=0.7)
        except:
            print_red("未找到重新寻找")

        print_green("开始钓鱼")
        pg.press("space")

        img_path = "images/fishing_ok.png"
        while True:
            sleep(1)
            try:
                pg.locateOnScreen(img_path, confidence=0.7)
                print_green("上鱼了，开始抬竿")
                pg.press("space")
                break
            except:
                print_red("还没上鱼，还不能抬竿")
        print_nol("等待6秒")
        pg.sleep(6)
        print_nol("连按空格")
        pg.press("space", presses=3, interval=0.5)

    sleep(1)
    # 检测是否钓鱼完成，可以撒饵
    print_nol("检测钓鱼是否完成")
    sleep(1)
    try:
        img_path = "images/fishery.png"
        pg.locateOnScreen(img_path, confidence=0.9)
        print_green("已经洒饵，钓鱼结束")
    except:
        print_nol("洒饵")
        pyautogui.press("space")
        print_nol("钓鱼结束")


def find_drones():
    """寻找无人机"""
    # 重置位置后，按下a键一秒钟
    print_nol("寻找无人机...")
    pg.press("r", presses=2, interval=0.5)
    pg.keyDown("a")
    sleep(1)
    pg.keyUp("a")
    print_nol("找到无人机")


def start():
    print_red("开始执行")
    num = 1
    while True:
        print_green("第{}次执行".format(num))

        # 检测农场
        timestamp_start = time.time()
        open_ymzx()
        find_drones()
        farm()
        # 检测渔场
        fishery()
        open_browser()
        # 计算耗时
        timestamp_end = time.time()
        computation_time = round(timestamp_end - timestamp_start, 2)
        print_nol("收获农场和渔场耗时：{}秒".format(computation_time))
        print_green("休息{}秒...".format(120 - computation_time))
        sleep(120 - computation_time)

        # 检测牧场
        timestamp_start = time.time()
        open_ymzx()
        find_drones()
        pasture()
        # 检测渔场
        fishery()
        open_browser()
        # 计算耗时
        timestamp_end = time.time()
        computation_time = round(timestamp_end - timestamp_start, 2)
        print_nol("收获农场和渔场耗时：{}秒".format(computation_time))
        print_green("休息{}秒...".format(120 - computation_time))
        sleep(120 - computation_time)

        # 判断是否执行了11次的倍数
        if num % 11 == 0:
            print_red("大概收获{}波".format(num // 11))
        num += 1


if __name__ == "__main__":
    # 执行任务
    start()
