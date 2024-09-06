from paddleocr import PaddleOCR

ocr = PaddleOCR()
result = ocr.ocr("fishpond.png")
print("识别结果：{}".format(result))
