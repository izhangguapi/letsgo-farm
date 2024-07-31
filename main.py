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
    print_nol("打开元梦之星")
    sleep(1)


def open_browser():
    """打开抖音"""
    os.system("open -a 'Google Chrome'")
    print_nol("打开浏览器刷抖音")
    sleep(1)
    pyautogui.press("down")
    sleep(1)
    pyautogui.press("up")


def find_drones():
    """寻找无人机"""
    # 重置位置后，按下a键一秒钟
    pyautogui.press("r", presses=2, interval=0.5)
    print_nol("寻找无人机")
    pyautogui.keyDown("a")
    sleep(1)
    pyautogui.keyUp("a")


def check_fram():
    """检查农场是否执行完成"""
    duration = 60
    timeout = duration
    with tqdm(total=duration) as pbar:
        pbar.set_description("等待农场执行...")
        for _ in range(duration):
            try:
                identify_img("farm_running", 0.9)
                pbar.update(timeout)
                break
            except:
                sleep(0.5)
                pbar.update(1)
                timeout -= 1
                sleep(1)
    if timeout <= 0:
        print_red("超时退出")
        return
    print_green("农场执行完成")


def farm():
    """无人机前往农场"""
    # print("收获农场")
    # x, y = 1360, 715
    # pyautogui.click(x, y)
    find_drones()
    print_nol("无人机前往农场工作")
    pyautogui.press("Q")


def pasture():
    """无人机前往牧场"""
    # x, y = 1540, 640
    # pyautogui.click(x, y)
    find_drones()
    check_fram()
    print_nol("无人机前往牧场工作")
    pyautogui.press("E")


def fishpond():
    """收获渔场"""
    print_nol("正在走到渔场...")
    go_to_fishpond()
    try:
        print_green("开始识别成熟时间")
        screenshot_save("fishpond")
        time = OCR_time("fishpond")
        if time < 120:
            t = time - 7
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=t)
            print_nol("等待{}秒后开始钓鱼具体时间为{}".format(t, specific_time))
            sleep(t)
            go_to_fishpond()
        else:
            print_red("等待时间超过2分钟，跳过")
            return
    except:
        print_red("识别失败")

    for _ in range(2):
        try:
            print_nol("检测能否能够钓鱼...")
            identify_img("fishing", 0.7)
        except:
            print_red("不能钓鱼，进行撒饵")
            pyautogui.press("space")
            print_green("钓鱼结束")
            return

        print_green("开始钓鱼")
        pyautogui.press("space")

        duration = 40
        timeout = duration
        with tqdm(total=duration) as pbar:
            pbar.set_description("等待上鱼...")
            for _ in range(duration):
                sleep(0.2)
                try:
                    identify_img("fishing_ok", 0.8)
                    pbar.update(timeout)
                    break
                except:
                    pbar.update(1)
                    timeout -= 1
            if timeout <= 0:
                print_red("等待超时")
                return
        print_green("上鱼了，开始抬竿")
        pyautogui.press("space")
        print_nol("等待7秒")
        sleep(7)
        print_nol("跳过钓鱼结算界面")
        pyautogui.press("g", presses=5, interval=1)

    # 检测是否钓鱼完成，可以撒饵
    # try:
    #     sleep(1)
    #     print_nol("检测是否撒饵")
    #     identify_img("fishpond_level", 0.7)
    #     print_green("撒饵")
    #     pyautogui.press("space")

    # except:
    #     print_green("已经撒饵，钓鱼结束")


def start():
    open_ymzx()
    # print_green("3秒后开始执行")
    # sleep(3)
    # num = 1
    while True:
        # print_green("第{}次执行".format(num))
        timestamp_start = datetime.datetime.now()
        # # 检测农场
        # timestamp_start = time.time()
        # open_ymzx()
        # go_to_farm()

        farm()
        fishpond()
        pasture()
        # 检测渔场
        # open_browser()
        # # 计算耗时
        # timestamp_end = time.time()
        # computation_time = round(timestamp_end - timestamp_start, 2)
        # print_nol("收获农场和渔场耗时：{}秒".format(computation_time))
        # print_green("休息{}秒...".format(120 - computation_time))
        # sleep(120 - computation_time)

        # 检测牧场
        # open_ymzx()

        # 检测渔场
        # fishpond()
        # open_browser()
        # 计算耗时
        timestamp_end = datetime.datetime.now()
        computation_time = timestamp_end - timestamp_start
        # computation_time = round(timestamp_end - timestamp_start, 2)
        t = 240 - computation_time.total_seconds()
        print_nol(
            "本次任务耗时：{}秒".format(round((computation_time).total_seconds(), 2))
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
    # open_ymzx()
    start()
