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
    find_drone()
    duration = 100
    timeout = duration
    minimum_progress = 300 / duration
    clear_progressbar()
    print_log("等待农场执行...")
    for _ in range(duration):
        update_progressbar(minimum_progress)
        timeout -= 1
        try:
            identify_img("farm_running", 0.8)
            update_progressbar(timeout * minimum_progress)
            break
        except:
            sleep(1)
        if timeout <= 0:
            print_log("超时，停止检测", "red")
            clear_progressbar()
            return
    print_log("农场执行完成", "green")


def identify_farm():
    """识别农场是否成熟"""
    # 前往农场第一块地
    go_to_farm()
    try:
        print_log("正在识别农场成熟时间...")
        screenshot_save("farm")
        time = OCR_time("farm")
        if time < 120:
            # 根据实际情况调整，如果不加时间会导致无人机收获的时间比后续成熟的快，导致后面的作物收获不了
            time = time + 5
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=time)
            print_log(
                "等待{}秒后开始收获具体时间为{}".format(time, specific_time), "green"
            )
            sleep(time)
            check_fram()
            farm_work()
        elif time < 240:
            time = time * 0.75 + 5
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=time)
            print_log(
                "等待{}秒后开始收获具体时间为{}".format(time, specific_time), "green"
            )
            sleep(time)
            check_fram()
            farm_work()
        else:
            print_log("等待时间超过2分钟，跳过", "red")
            check_fram()
            return
    except:
        print_log("识别失败可能成熟，操作无人机去农场工作", "red")
        check_fram()
        farm_work()


def farm_work():
    """无人机前往农场"""
    find_drone()
    print_log("无人机前往农场工作")
    pyautogui.press("Q")


def pasture_work():
    """无人机前往牧场"""
    find_drone()
    print_log("无人机前往牧场工作")
    pyautogui.press("E")


# 开始钓鱼
def fishing():
    """开始钓鱼"""
    for i in range(2):
        try:
            print_log("检测是否能钓鱼")
            identify_img("fishing", 0.8)
            print_log("可以钓鱼", "green")
            clear_progressbar()
            print_log("开始第{}次钓鱼".format(i), "green")
            pyautogui.press("space")
            sleep(3)
            duration = 30
            timeout = duration
            minimum_progress = 300 / duration
            print_log("等待上鱼...")
            for _ in range(duration):
                update_progressbar(minimum_progress)
                if timeout <= 0:
                    print_log("等待超时，退出钓鱼", "red")
                    clear_progressbar()
                    return
                timeout -= 1
                try:
                    identify_img("fishing_ok", 0.8)
                    update_progressbar(timeout * minimum_progress)
                    print_log("上鱼了，开始抬竿", "green")
                    pyautogui.press("space")
                    print_log("等待7秒")
                    sleep(7)
                    print_log("跳过钓鱼结算界面")
                    pyautogui.press("g", presses=5, interval=1)
                    break
                except:
                    sleep(0.2)

            print_log("钓鱼完成", "green")
        except:
            print_log("不能钓鱼", "red")
            return


def baiting():
    """撒饵"""
    try:
        print_log("检测是否撒饵")
        identify_img("fishpond_level", 0.7)
        print_log("未撒饵撒饵，执行撒饵", "red")
        pyautogui.press("space")
        print_log("撒饵成功", "green")
        return
    except:
        print_log("已经撒饵", "green")


def fishpond():
    """收获渔场"""
    go_to_fishpond()
    try:
        # print_green("开始识别成熟时间")
        print_log("正在识别鱼塘成熟时间...")
        screenshot_save("fishpond")
        time = OCR_time("fishpond")
        if time < 120:
            t = time - 10
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=t)
            print_log(
                "等待{}秒后开始钓鱼具体时间为{}".format(t, specific_time), "green"
            )
            sleep(t)
            go_to_fishpond()
            fishing()
        else:
            print_log("等待时间超过2分钟，跳过", "red")
            return
    except:
        print_log("识别失败", "red")
        fishing()
    baiting()


def start():
    # mac用户
    open_ymzx()
    # windows用户
    # print_log("请在5秒内打开元梦之星")
    # sleep(5)
    while True:
        timestamp_start = datetime.datetime.now()
        # 无人机前往农场工作
        farm_work()
        # 收获鱼塘
        fishpond()
        # 识别农场
        identify_farm()
        # 无人机前往牧场工作
        pasture_work()
        # 计算耗时
        timestamp_end = datetime.datetime.now()
        computation_time = timestamp_end - timestamp_start
        t = 300 - computation_time.total_seconds()
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
