import psutil

# 获取当前所有进程的信息
# for proc in psutil.process_iter(["pid", "name", "exe"]):
#     print(proc.info)

# 也可以通过进程ID获取单个进程的信息
# pid = os.getpid()
# process = psutil.Process(pid)
# print(process.name())
# print(process.exe())
# print(process.cmdline())


# 假设我们要获取PID为1234的进程的所有子孙进程
pid = 53564
proc = psutil.Process(pid)
print(proc.name(), proc.exe())

# # 获取子孙进程列表
# children_processes = parent_process.children(recursive=True)

# # 打印子孙进程的PID
# for child in children_processes:
#     print(child.pid,child.name())
