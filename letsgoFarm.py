import myTools as mt


def find_drone():
    """寻找无人机"""
    # 重置位置后，按下a键一秒钟
    wcl.key_press("r")
    mt.print_log("寻找无人机")
    wcl.key_press("a", 1)


def farm_work():
    """无人机前往农场"""
    find_drone()
    mt.print_log("无人机前往农场工作")
    wcl.mouse_move_press(position["farm_btn"])
    # mt.sleep(100)


def pasture_work():
    """无人机前往牧场"""
    find_drone()
    mt.print_log("无人机前往牧场工作")
    wcl.mouse_move_press(position["pasture_btn"])
    mt.sleep(30)


def fishpond_work():
    """无人机前往鱼塘"""
    find_drone()
    mt.print_log("无人机前往鱼塘工作")
    wcl.mouse_move_press(position["fishpond_btn"])
    mt.sleep(6)
    for _ in range(30):
        wcl.mouse_move_press(position["blank"])
        mt.sleep(0.2)
    clw.set_now()


# def farm():
#     # 前往农场第一块地
#     go_to_farm()
#     mt.sleep(1)
#     try:
#         print("正在识别农场成熟时间...")
#         idt.screenshot_save("farm")
#         time = idt.OCR_time("farm")
#         # 成熟时间小于2分钟就等待2分钟再启动无人机，等待70秒执行农场
#         if time < 120:
#             # 根据实际情况调整，如果不加时间会导致无人机收获的时间比后续成熟的快，导致后面的作物收获不了
#             specific_time = datetime.now() + datetime.timedelta(seconds=time)
#             print("等待{}秒后开始收获具体时间为{}".format(time, specific_time), "green")
#             sleep(time)
#         # 成熟时间小于4分钟就等待4分钟*0.75再启动无人机，等待105秒执行农场
#         elif time < 240:
#             time = time * 0.75
#             specific_time = datetime.now() + datetime.timedelta(seconds=time)
#             print("等待{}秒后开始收获具体时间为{}".format(time, specific_time), "green")
#             sleep(time)
#             start_time = farm_work()
#             return start_time + datetime.timedelta(seconds=105)
#         # 成熟时间大于4分钟就直接浇水，等待45秒执行农场
#         else:
#             print("等待时间超过4分钟，执行浇水", "red")
#             start_time = farm_work()
#             return start_time + datetime.timedelta(seconds=45)
#     except:
#         print("识别失败可能已成熟，操作无人机去农场工作", "red")

#     start_time = farm_work()
#     return start_time + datetime.timedelta(seconds=75)


# def fishing(num=2):
#     """开始钓鱼"""
#     for i in range(int(num)):
#         try:
#             print("检测能否钓鱼")
#             idt.identify_img("fishpond_level", 0.8)
#             print("不能钓鱼", "red")
#         except:
#             print("可以钓鱼", "green")
#             print("开始第{}次钓鱼".format(i + 1), "green")
#             wcl.key_press("space")
#             print("等待上鱼...")
#             mt.sleep(6)
#             print("开始抬竿")
#             wcl.key_press("space")
#             print("跳过钓鱼结算界面")
#             for i in range(5):
#                 wcl.mouse_move_press(x=780, y=570)
#                 # vkb.key_press("g", presses=5, interval=1)
#             mt.sleep(1)
#     print("执行撒饵", "red")
#     wcl.key_press("space")
#     print("钓鱼完成", "green")

def all_work():
    """农场"""
    find_drone()
    mt.print_log("无人机执行全部工作")
    wcl.key_press("q")

def farm():
    """农场"""
    if mt.check_settings("farm"):
        farm_work()


def pasture():
    """牧场"""
    if mt.check_settings("pasture"):
        pasture_work()


def fishpond():
    """鱼塘"""
    if mt.check_settings("fishpond"):
        go_to("fishpond")
        mt.print_log("正在识别鱼塘成熟时间...")
        # 获取截图的区域
        position_time = position["time"]
        # 截图并且获取图片路径
        img_path = wcl.screenshot_window(position_time)
        # 识别图片中的时间
        time = mt.ocr_img(img_path)
        if len(time) < 1:
            mt.print_log("未识别到时间，跳过", "red")
            return
        mt.print_log(f"识别到信息: {time}", "green")
        time = time[0]
        if "可钓" in time:
            fishpond_work()
            return True
        # 将时间转为秒
        s = mt.convert_to_seconds(time)
        if s < 180:
            t = s - 3
            specific_time = clw.computing_specific_time(seconds=t)
            mt.print_log(
                "等待{}秒后开始钓鱼具体时间为{}".format(t, specific_time), "green"
            )
            mt.sleep(t)
            fishpond_work()
            return True
        else:
            mt.print_log("等待时间超过3分钟，跳过")
            return False


def cancel_lens_assist():
    lens = position["lens"]
    mt.print_log("取消镜头辅助")
    for i in lens:
        wcl.mouse_move_press(i)
        mt.sleep(1)



def go_to(where=None):
    if where == "farm":
        data = key["go_to_farm"]
        mt.print_log("前往农场...")
    elif where == "pasture":
        data = key["go_to_pasture"]
        mt.print_log("前往牧场...")
    elif where == "fishpond":
        data = key["go_to_fishpond"]
        mt.print_log("前往鱼塘...")
        for i in data:
            if i["type"] == "press":
                wcl.key_press(i["details"])
            elif i["type"] == "down":
                wcl.key_down(i["details"])
            elif i["type"] == "up":
                wcl.key_up(i["details"])
            elif i["type"] == "sleep":
                mt.sleep(i["details"])
    else:
        mt.print_log("未知地点")


def initialization():
    """初始化"""
    global wcl, clw, key, position
    mt.print_log(f"检测窗口句柄: {mt.hwnd}")
    if not mt.hwnd:
        mt.print_log("未找到窗口句柄，退出挂机")
        return
    # 初始化窗口控制类,时间等待控制类
    wcl = mt.WindowController(mt.hwnd)
    clw = mt.CalculationWaiting()

    # 获取按键和坐标配置
    key = mt.get_key()
    position = mt.get_position()

    # 点击一下跳跃
    wcl.mouse_move_press(position["jump"])
    mt.sleep(1)
    if mt.lgf_config["cancel_lens_assist"]:
        cancel_lens_assist()

def start():
    # 初始化
    initialization()
    mt.print_log("开始挂机")
    while not mt.exit_event.is_set():
        # 记录开始时间
        clw.set_now()
        # 解除省电模式
        wcl.mouse_move_press(position["jump"])
        mt.sleep(1)
        # 执行鱼塘工作
        all_work()
        # 计算耗时
        clw.computing_time()
    mt.print_log("停止挂机")
