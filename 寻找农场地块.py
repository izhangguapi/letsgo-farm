import pyautogui as pg
import time, random
from letsgoFarm import go_to_farm, sleep


pg.FAILSAFE = False
# pg.PAUSE = 1

# 获取屏幕大小
screen_width, screen_height = pg.size()
screen_width = screen_width / 2 + 50
screen_height = screen_height / 2
# 将鼠标移动到屏幕中央

# 设置鼠标移动的距离（像素）和时间（秒）
time.sleep(3)
duration = 1


def random_move():
    if random.randint(0, 1):
        return 0.56
    else:
        return 0.57


# 拖动鼠标
go_to_farm()
sleep(0.5)
pg.moveTo(screen_width, screen_height, duration=0)
pg.dragRel(335, duration=duration, button="left")
for i in range(4):
    sleep(0.5)
    pg.keyDown("w")
    sleep(random_move())
    pg.keyUp("w")
sleep(0.5)
pg.moveTo(screen_width, screen_height, duration=0)
pg.dragRel(-222, duration=duration, button="left")
sleep(0.5)
pg.keyDown("w")
sleep(random_move())
pg.keyUp("w")
sleep(0.5)
pg.moveTo(screen_width, screen_height, duration=0)
pg.dragRel(-222, duration=duration, button="left")
for i in range(4):
    sleep(0.5)
    pg.keyDown("w")
    sleep(random_move())
    pg.keyUp("w")


sleep(0.5)
pg.moveTo(screen_width, screen_height, duration=0)
pg.dragRel(222, duration=duration, button="left")
sleep(0.5)
pg.keyDown("w")
sleep(random_move())
pg.keyUp("w")
sleep(0.5)
pg.moveTo(screen_width, screen_height, duration=0)
pg.dragRel(222, duration=duration, button="left")
for i in range(4):
    sleep(0.5)
    pg.keyDown("w")
    sleep(random_move())
    pg.keyUp("w")


# sleep(0.5)
# pg.moveTo(screen_width, screen_height, duration=0)
# pg.dragRel(-223, duration=duration, button="left")
# sleep(0.5)
# pg.keyDown("w")
# sleep(random_move())
# pg.keyUp("w")
# sleep(0.5)
# pg.moveTo(screen_width, screen_height, duration=0)
# pg.dragRel(-222, duration=duration, button="left")
# for i in range(4):
#     sleep(0.5)
#     pg.keyDown("w")
#     sleep(random_move())
#     pg.keyUp("w")

# sleep(0.5)
# pg.moveTo(screen_width, screen_height, duration=0)
# pg.dragRel(223, duration=duration, button="left")
# sleep(0.5)
# pg.keyDown("w")
# sleep(random_move())
# pg.keyUp("w")
# sleep(0.5)
# pg.moveTo(screen_width, screen_height, duration=0)
# pg.dragRel(222, duration=duration, button="left")
# for i in range(4):
#     sleep(0.5)
#     pg.keyDown("w")
#     sleep(random_move())
#     pg.keyUp("w")

# sleep(0.5)
# pg.moveTo(screen_width, screen_height, duration=0)
# pg.dragRel(-223, duration=duration, button="left")
# sleep(0.5)
# pg.keyDown("w")
# sleep(random_move())
# pg.keyUp("w")
# sleep(0.5)
# pg.moveTo(screen_width, screen_height, duration=0)
# pg.dragRel(-222, duration=duration, button="left")
# for i in range(4):
#     sleep(0.5)
#     pg.keyDown("w")
#     sleep(random_move())
#     pg.keyUp("w")
