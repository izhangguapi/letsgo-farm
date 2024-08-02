from identify import *
from myTools import *

"""
农场:farm
牧场:pasture
鱼塘:fishpond
钓鱼按钮:fishing
可以钓鱼:fishing_ok
鱼塘等级:fishpond_level
无人机(用于识别按钮):drone
"""
os.system("open -a '元梦之星-云游戏-快捷方式'")
pyautogui.sleep(1)
# go_to_fishpond()
screenshot_show(identify_img("farm_running", 0.9))
# OCR_time("fishpond")

# for i in range(10):
#     try:
#         identify_img("fishing", 0.4)
#     except:
#         continue
# screenshot_save("fishpond")
# identify_img("fishing", 0.8)

