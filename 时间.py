from datetime import datetime
 
# 字符串时间格式
str_time = "00:44:55"
 
# 转换为时间戳
timestamp = datetime.strptime(str_time, "%H:%M:%S").timestamp()

print(timestamp)