import time,datetime

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



import time
 
# 动态进度条函数
def progress_bar(total, progress):
    # 计算进度百分比
    percent = (progress / total) * 100
    # 打印动态进度条
    print(f'\rProgress: [{progress}/{total}] {percent:.2f}%', end='')
 
# 模拟一个长度为10的任务
total = 10
for i in range(1, total + 1):
    # 模拟任务进度
    time.sleep(0.5)  # 假设每个阶段需要0.5秒
    progress_bar(total, i)  # 更新进度条
 
# 结束后打印换行
print()