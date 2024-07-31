from paddleocr import PaddleOCR
import pyautogui, os,time
from tqdm import tqdm
from myTools import *


# import cv2


# 识别钓鱼按钮
def identify_img(img, confidence):
    """识别图片"""
    img_path = "images/identify/" + img + ".png"
    location = pyautogui.locateOnScreen(img_path, confidence=confidence)
    # location = (location[0] // 2, location[1] // 2, location[2] // 2, location[3] // 2)
    return location




def screenshot_show(location):
    """截图并显示"""
    location = (location[0] // 2, location[1] // 2, location[2] // 2, location[3] // 2)
    image = pyautogui.screenshot(region=location)
    image.show()  # 显示图片


def screenshot_save(img):
    """
    截图并保存
    """
    img_path = "images/identify/" + img + ".png"
    location = pyautogui.locateOnScreen(img_path, confidence=0.7)

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
    result = ocr.ocr(img=img_path, cls=False)
    print(result)
    print("识图信息：", result)

    # 获取识别结果中的时间以

    # 识别文字，获取耗时
    time = result[0][0][1][0].split("后")[0]
    spend = result[0][0][1][1]
    print("识图耗时：", spend)
    print("图片中的时间：", time)

    # 判断最大事件为小时还是分钟
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
    print("转为秒：", seconds)
    return seconds - int(spend)


"""
农场:farm
牧场:pasture
鱼塘:fishpond
"""
# os.system("open -a '元梦之星-云游戏-快捷方式'")
# pyautogui.sleep(1)
# go_to_fishery()
# identify_img_show("fishing", 0.8)
# identify_img("fishing", 0.8)
# screenshot("pasture")
# OCR_time("pasture")
# identify_img("fishing", 0.8)