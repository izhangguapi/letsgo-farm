import myTools as mt
import identify_test as idt
from paddleocr import PaddleOCR
import numpy as np
import tempfile, os
from PIL import Image


# wcl = mt.WindowController(3147388)
wcl = mt.WindowController(5113718)
fp = wcl.screenshot_window(position=(25, 273, 120, 25))
# fp = wcl.screenshot_window(position=(25,140,120,160))
# fp = wcl.screenshot_window()

time = mt.ocr_img(fp)[0]

s = mt.convert_to_seconds(time)
print(s)

# print(text[0])
# print(text[1])
