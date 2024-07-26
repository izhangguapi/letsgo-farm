from paddleocr import PaddleOCR
import pyautogui, os
# import cv2

# 识别钓鱼按钮
def identify_img(img, confidence):
    """识别图片"""
    img_path = "images/identify/" + img + ".png"
    pyautogui.locateOnScreen(img_path, confidence=confidence)


    

def screenshot(img):
    """
    截图并保存
    """
    img_path = "images/identify/" + img + ".png"
    location = pyautogui.locateOnScreen(img_path, confidence=0.8)

    # 苹果系统专用，没有次行代码会导致截图位置错误，Windows未测试，如果出现截图不正确请注释下一行
    location = (location[0] // 2, location[1] // 2, location[2] // 2, location[3] // 2)

    image = pyautogui.screenshot(region=location)
    image.save("images/temp/" + img + ".png")  # 保存位置
    # image = cv2.imread("images/temp/" + img + ".png")
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray_image.show()
    # image.show()  # 显示图片


def OCR_time(img):
    """
    识别图片中的时间，并将其转为秒
    参数:
    img(str): 图片名称,会自动添加

    返回值: 返回图片中时间转为秒，以及图片识别耗时
    """
    img_path = "images/temp/" + img + ".png"

    # 创建一个PaddleOCR对象
    ocr = PaddleOCR()
    # 使用PaddleOCR对象进行图片识别，不进行文本检测，角度分类器
    result = ocr.ocr(img=img_path, det=False, cls=False)
    print(result)

    # 获取识别结果中的时间以
    time = ''
    try:
        time = result[0][0][0].split("后")[0]
    except:
        print("未识别到时间")
        print("图片中的信息：", result)
        return 0, 0
    # 识别耗时
    spend = int(result[0][0][1]) + 1
    # 判断最大事件为小时还是分钟
    seconds = 0
    if "时" in time:
        seconds = time.split("分")[0].split("小时")
        seconds = (int(seconds[0]) * 60 + int(seconds[1])) * 60
    elif "分" in time:
        seconds = time.split("秒")[0].split("分")
        seconds = int(seconds[0]) * 60 + int(seconds[1])
    else:
        seconds = int(time.split("秒")[0])

    print("将图片中时间", time, "转为秒：", seconds)
    print("图片识别耗时：", spend, "秒")
    return seconds


# os.system("open -a '元梦之星-云游戏-快捷方式'")
# pyautogui.sleep(1)
# screenshot("pasture")
# time_ocr("fishery")
