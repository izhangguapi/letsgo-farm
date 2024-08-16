from myTools import *
from identify import *


def open_ymzx():
    """打开元梦"""
    print_log("打开元梦之星")
    os.system("open -a '元梦之星-云游戏-快捷方式'")
    sleep(1)


def open_browser():
    """打开抖音"""
    os.system("open -a 'Google Chrome'")
    print_log("打开浏览器刷抖音")
    sleep(1)
    pyautogui.press("down")
    sleep(1)
    pyautogui.press("up")


def go_to_farm():
    """走到农场"""
    pyautogui.press("r", presses=2, interval=0.5)
    print_log("开始走到农场...")
    pyautogui.keyDown("w")
    pyautogui.keyDown("a")
    sleep(4.2)
    pyautogui.keyUp("a")
    sleep(0.3)
    pyautogui.keyUp("w")
    print_log("到达农场", "green")
    sleep(1)


def go_to_pasture():
    """走到牧场"""
    pyautogui.press("r")
    print_log("开始走到牧场...")
    pyautogui.keyDown("w")
    sleep(0.8)
    pyautogui.keyDown("d")
    sleep(1.2)
    pyautogui.keyUp("w")
    pyautogui.keyUp("d")
    print_log("到达牧场", "green")
    # sleep(1)


def go_to_fishpond():
    """走到鱼塘"""
    pyautogui.press("r")
    print_log("开始走到鱼塘...")
    pyautogui.keyDown("w")
    pyautogui.keyDown("a")
    sleep(0.5)
    pyautogui.keyUp("a")
    sleep(5.7)
    pyautogui.keyUp("w")
    print_log("到达鱼塘", "green")
    # sleep(1)


def find_drone():
    """寻找无人机"""
    # 重置位置后，按下a键一秒钟
    pyautogui.press("r", presses=2, interval=0.5)
    print_log("寻找无人机")
    pyautogui.keyDown("a")
    sleep(1)
    pyautogui.keyUp("a")


def farm_work():
    """无人机前往农场"""
    start_time = datetime.datetime.now()
    find_drone()
    print_log("无人机前往农场工作")
    pyautogui.press("Q")
    return start_time


def pasture_work():
    """无人机前往牧场"""
    find_drone()
    print_log("无人机前往牧场工作")
    pyautogui.press("E")


def farm():
    # 前往农场第一块地
    go_to_farm()
    sleep(1)
    try:
        print_log("正在识别农场成熟时间...")
        screenshot_save("farm")
        time = OCR_time("farm")
        # 成熟时间小于2分钟就等待2分钟再启动无人机，等待70秒执行农场
        if time < 120:
            # 根据实际情况调整，如果不加时间会导致无人机收获的时间比后续成熟的快，导致后面的作物收获不了
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=time)
            print_log(
                "等待{}秒后开始收获具体时间为{}".format(time, specific_time), "green"
            )
            sleep(time)
        # 成熟时间小于4分钟就等待4分钟*0.75再启动无人机，等待105秒执行农场
        elif time < 240:
            time = time * 0.8
            specific_time = datetime.datetime.now() + datetime.timedelta(seconds=time)
            print_log(
                "等待{}秒后开始收获具体时间为{}".format(time, specific_time), "green"
            )
            sleep(time)
            start_time = farm_work()
            return start_time + datetime.timedelta(seconds=105)
        # 成熟时间大于4分钟就直接浇水，等待45秒执行农场
        else:
            print_log("等待时间超过4分钟，执行浇水", "red")
            start_time = farm_work()
            return start_time + datetime.timedelta(seconds=45)
    except:
        print_log("识别失败可能已成熟，操作无人机去农场工作", "red")

    start_time = farm_work()
    return start_time + datetime.timedelta(seconds=75)


def fishing(num=2):
    """开始钓鱼"""
    for i in range(int(num)):
        try:
            print_log("检测能否钓鱼")
            identify_img("fishpond_level", 0.8)
            print_log("不能钓鱼", "red")
        except:
            print_log("可以钓鱼", "green")
            print_log("开始第{}次钓鱼".format(i + 1), "green")
            pyautogui.press("space")
            print_log("等待上鱼...")
            sleep(6)
            print_log("开始抬竿")
            pyautogui.press("space")
            # print_log("等待7秒")
            # sleep(7)
            print_log("跳过钓鱼结算界面")
            pyautogui.press("g", presses=35, interval=0.2)
            sleep(1)

    print_log("执行撒饵", "green")
    pyautogui.press("space")
    print_log("钓鱼完成", "green")


def baiting():
    """撒饵"""
    try:
        print_log("检测是否撒饵")
        identify_img("fishpond_level", 0.8)
        print_log("撒饵成功", "green")
        return
    except:
        print_log("已经撒饵", "green")


def fishpond():
    """收获渔场"""
    go_to_fishpond()
    try:
        print_log("正在识别鱼塘成熟时间...")
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
            fishing()
        else:
            print_log("等待时间超过2分钟，跳过", "red")
            return
    except:
        print_log("识别失败", "red")
        fishing()


def start():
    print_log("开始运行", "green")
    # mac用户
    open_ymzx()
    # windows用户
    # print_log("请在5秒内打开元梦之星")
    # sleep(5)
    while not exit_event.is_set():
        start_time = datetime.datetime.now()
        # 识别农场进行工作
        # wait_s = farm()
        # 执行牧场工作
        farm_work()
        # 收获鱼塘
        fishpond()
        # 计算耗时
        t = start_time + datetime.timedelta(seconds=105)
        wait = (t - datetime.datetime.now()).total_seconds()
        print_log("等待{}秒后前往牧场".format(wait))
        print_log("具体时间为：{}".format(t), "green")
        if wait > 0:
            sleep(wait)
        # 执行牧场工作
        pasture_work()
        # 计算耗时
        end_time = datetime.datetime.now()
        computation_time = end_time - start_time
        t = 300 - computation_time.total_seconds()
        print_log(
            "本次任务耗时：{}秒，休息{}秒，".format(
                round((computation_time).total_seconds(), 2), t
            ),
            "green",
        )
        print_log(
            "下次运行时间：{}".format(end_time + datetime.timedelta(seconds=t)),
            "green",
        )
        sleep(t)

    print_log("程序被停止", "red")
