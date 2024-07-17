import pyautogui as pg

# 走到农场地块
pg.sleep(3)
pg.press("r")
pg.keyDown("a")
pg.sleep(1)
pg.keyUp("a")
pg.keyDown("w")
pg.sleep(2)
pg.keyUp("w")
# 走到牧场地块
pg.sleep(3)
pg.press("r")
pg.keyDown("d")
pg.sleep(1)
pg.keyUp("d")
pg.keyDown("w")
pg.sleep(2)
pg.keyUp("w")
