from paddleocr import PaddleOCR
import pyautogui, os, time
from tqdm import tqdm
from myTools import *


# import cv2


# 识别钓鱼按钮
def identify_img(img, confidence):
    """识别图片"""
    img_path = "images/identify/" + img + ".png"
    location = pyautogui.locateOnScreen(img_path, confidence=confidence)
    return location


def screenshot_show(location):
    """截图并显示"""
    # macos苹果系统专用，没有次行代码会导致截图位置错误，windows请注释下一行
    location = (location[0] // 2, location[1] // 2, location[2] // 2, location[3] // 2)
    # windows专用，mac请注释下一行
    # location = (int(location[0]), int(location[1]), int(location[2]), int(location[3]))
    image = pyautogui.screenshot(region=location)
    # 显示图片
    image.show()


def screenshot_save(img):
    """
    截图并保存
    """
    img_path = "images/identify/" + img + ".png"
    location = pyautogui.locateOnScreen(img_path, confidence=0.7)
    # macos苹果系统专用，没有次行代码会导致截图位置错误，windows请注释下一行
    location = (location[0] // 2, location[1] // 2, location[2] // 2, location[3] // 2)
    # windows专用，mac请注释下一行
    # location = (int(location[0]), int(location[1]), int(location[2]), int(location[3]))
    image = pyautogui.screenshot(region=location)
    # 保存位置
    image.save("images/temp/" + img + ".png")


def OCR_time(img):
    """
    识别图片中的时间，并将其转为秒
    参数:
    img(str): 图片名称,会自动添加

    返回值: 返回图片中时间转为秒，以及图片识别耗时
    """
    # 创建一个PaddleOCR对象
    ocr = PaddleOCR()
    # 使用PaddleOCR对象进行图片识别
    img_path = "images/temp/" + img + ".png"
    result = ocr.ocr(img=img_path, cls=False)
    print_log("识别结果：{}".format(result),"green")
    # 识别文字，获取耗时
    time = result[0][0][1][0].split("后")[0]
    spend = result[0][0][1][1]
    print_log("剩余时间：{}，耗时：{}".format(time, spend),"green")

    # 将得到的时间转为秒
    h = m = s = 0
    if "时" in time:
        temp = time.split("小时")
        h = int(temp[0])
        time = temp[1]
    if "分" in time:
        temp = time.split("分")
        m = int(temp[0])
        time = temp[1]
    if "秒" in time:
        s = int(time.split("秒")[0])
    seconds = h * 3600 + m * 60 + s
    print_log("转为秒：{}秒".format(seconds),"green")
    return seconds - int(spend)
