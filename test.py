from myTools import *
import os


# print(get_datetime())
# os.system("open -a '元梦之星-云游戏-快捷方式'")
# sleep(1)
# pyautogui.press("r")
# # print_log("正在走到鱼塘...")
# pyautogui.keyDown("w")
# pyautogui.keyDown("a")
# sleep(0.3)
# pyautogui.keyUp("a")
# sleep(3)
# pyautogui.keyDown("d")
# sleep(0.5)
# pyautogui.keyUp("d")
# sleep(1.8)
# pyautogui.keyUp("w")
# sleep(1)
# import time,datetime

# now = time.time()
# timeArray = time.localtime(now+300)
# print(timeArray)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print(otherStyleTime)


# print(time.strftime("[%Y-%m-%d %H:%M:%S:%m] - ", time.localtime()))


# now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]   #2023-02-07 01:48:26.09保留两位小数
# print(now_time)    # 2023-02-07 01:43:07.154610

# duration = datetime.timedelta(seconds=3)

# 获取当前日期和时间
# now = datetime.datetime.now()
# print(now)

# 计算目标日期和时间
# target = now + duration
# print(target)
# 格式化输出目标日期和时间
# target_str = target.strftime("%Y-%m-%d %H:%M:%S.%f")

# print(target_str)
# d = 300 - c.total_seconds()
# print("休息{}秒，下次运行时间：{}".format(c , datetime.now() + datetime.timedelta(seconds=c)))

# print(datetime.now() + datetime.second(300))

# print()  # 4.0
# time = "23秒"

# h = m = s = 0
# if "时" in time:
#     temp = time.split("小时")
#     h = int(temp[0])
#     time = temp[1]
# if "分" in time:
#     temp = time.split("分")
#     m = int(temp[0])
#     time = temp[1]
# if "秒" in time:
#     s = int(time.split("秒")[0])


# print(h)
# print(m)
# print(s)

# print("将图片中时间", time, "转为秒：", seconds)
# print("图片识别耗时：", spend, "秒")


# import time

# # 动态进度条函数
# def progress_bar(total, progress):
#     # 计算进度百分比
#     percent = (progress / total) * 100
#     # 打印动态进度条
#     print(f'\rProgress: [{progress}/{total}] {percent:.2f}%', end='')

# # 模拟一个长度为10的任务
# total = 10
# for i in range(1, total + 1):
#     # 模拟任务进度
#     time.sleep(0.5)  # 假设每个阶段需要0.5秒
#     progress_bar(total, i)  # 更新进度条

# # 结束后打印换行
# print()


# import psutil

# # 获取所有进程信息
# proc = psutil.Process(25043)
# print(proc.cmdline())


# # 假设我们要获取PID为1234的进程的所有子孙进程
# pid = 25043

# # 使用psutil获取指定PID的进程
# parent_process = psutil.Process(pid)

# # 获取子孙进程列表
# children_processes = parent_process.children(recursive=True)

# # 打印子孙进程的PID
# for child in children_processes:
#     print(child.pid,child.name())

# import psutil

# # 获取当前所有进程的信息
# for proc in psutil.process_iter(['name', 'pid']):
#     print(proc.info)

# 或者只获取指定属性
# for proc in psutil.process_iter(['name', 'exe']):
#     print(proc.info)

# 也可以通过进程ID获取单个进程的信息
# pid = os.getpid()
# process = psutil.Process(pid)
# print(process.name())
# print(process.exe())
# print(process.cmdline())

# import tkinter, time
# from tkinter import ttk

# tk = tkinter.Tk()
# tk.geometry("150x120")


# def update_progressbar(window,p):
#     # 每次更新加1
#     p["value"] = p["value"] + 1
#     # 更新画面
#     window.update()


# p = ttk.Progressbar(tk, orient="horizontal", length=100, mode="determinate")
# p.pack(pady=20)


# button = tkinter.Button(tk, text="增加", command=lambda: update_progressbar(p))
# button.pack(pady=5)

# tk.mainloop()
