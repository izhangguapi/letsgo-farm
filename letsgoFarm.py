from myTools import *
from identify import *


def open_ymzx():
    """打开元梦"""
    os.system("open -a '元梦之星-云游戏-快捷方式'")
    print_log("打开元梦之星")
    # print_nol("打开元梦之星")
    # test_window.print_log("打开元梦之星")
    sleep(1)


def open_browser():
    """打开抖音"""
    os.system("open -a 'Google Chrome'")
    # print_nol("打开浏览器刷抖音")
    print_log("打开浏览器刷抖音")
    sleep(1)
    pyautogui.press("down")
    sleep(1)
    pyautogui.press("up")


def find_drone():
    """寻找无人机"""
    # 重置位置后，按下a键一秒钟
    pyautogui.press("r", presses=2, interval=0.5)
    print_log("寻找无人机")
    # print_nol("寻找无人机")
    pyautogui.keyDown("a")
    sleep(1)
    pyautogui.keyUp("a")


def check_fram():
    """检查农场是否执行完成"""
    duration = 100
    timeout = duration
    minimum_progress = 200 / duration
    clear_progressbar()
    print_log("等待农场执行...")
    for _ in range(duration):
        update_progressbar(minimum_progress)
        timeout -= 1
        try:
            identify_img("farm_running", 0.9)
            update_progressbar(timeout * minimum_progress)
            break
        except:
            sleep(1)
        if timeout <= 0:
            print_log("超时，停止检测", "red")
            clear_progressbar()
            return
    print_log("农场执行完成", "green")


def farm():
    """无人机前往农场"""
    find_drone()
    print_log("无人机前往农场工作")
    pyautogui.press("Q")


def pasture():
    """无人机前往牧场"""
    find_drone()
    check_fram()
    # print_nol("无人机前往牧场工作")
    print_log("无人机前往牧场工作")
    pyautogui.press("E")


def fishpond():
    """收获渔场"""
    go_to_fishpond()
    try:
        # print_green("开始识别成熟时间")
        print_log("开始识别成熟时间")
        screenshot_save("fishpond")
        time = OCR_time("fishpond")
        if time < 120:
            t = time - 8
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=t)
            print_log(
                "等待{}秒后开始钓鱼具体时间为{}".format(t, specific_time), "green"
            )
            sleep(t)
            go_to_fishpond()
        else:
            print_log("等待时间超过2分钟，跳过", "red")
            return
    except:
        print_log("识别失败", "red")

    # 检测是否撒饵
    try:
        print_log("检测是否撒饵")
        identify_img("fishpond_level", 0.7)
        print_log("撒饵", "green")
        pyautogui.press("space")
        return
    except:
        print_log("已经撒饵", "red")

    for _ in range(2):
        print_log("开始钓鱼", "green")
        pyautogui.press("space")
        sleep(3)

        duration = 40
        timeout = duration
        minimum_progress = 200 / duration
        clear_progressbar()
        print_log("等待上鱼...")
        for _ in range(duration):
            sleep(0.2)
            try:
                identify_img("fishing_ok", 0.8)
                update_progressbar(timeout * minimum_progress)
                break
            except:
                update_progressbar(minimum_progress)
                timeout -= 1
        if timeout <= 0:
            print_log("等待超时，退出钓鱼", "red")
            clear_progressbar()
            return
        # with tqdm(total=duration) as pbar:
        #     pbar.set_description(get_date() + "等待上鱼...")

        #     for _ in range(duration):
        #         sleep(0.2)
        #         try:
        #             identify_img("fishing_ok", 0.8)
        #             pbar.update(timeout)
        #             break
        #         except:
        #             pbar.update(1)
        #             timeout -= 1
        #     if timeout <= 0:
        #         print_log("等待超时，退出钓鱼","red")
        #         return
        print_log("上鱼了，开始抬竿", "green")
        pyautogui.press("space")
        print_log("等待7秒")
        sleep(7)
        print_log("跳过钓鱼结算界面")
        pyautogui.press("g", presses=5, interval=1)

    print_log("钓鱼完成，进行撒饵", "green")
    sleep(1)
    pyautogui.press("space")


def start():
    open_ymzx()
    while True:
        timestamp_start = datetime.datetime.now()
        # 农场
        farm()
        # 鱼塘
        fishpond()
        # 牧场
        pasture()
        # 计算耗时
        timestamp_end = datetime.datetime.now()
        computation_time = timestamp_end - timestamp_start
        t = 240 - computation_time.total_seconds()
        print_log(
            "本次任务耗时：{}秒，休息{}秒，".format(
                round((computation_time).total_seconds(), 2), t
            ),
            "green",
        )
        print_log(
            "下次运行时间：{}".format(timestamp_end + datetime.timedelta(seconds=t)),
            "green",
        )
        sleep(t)
