# 定义ANSI转义代码
class ANSI:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[m"


# 打印红色文本的函数
def print_red(text):
    print(ANSI.RED + text + ANSI.RESET)


def print_green(text):
    print(ANSI.GREEN + text + ANSI.RESET)


# 使用函数打印红色文本
print_red("这是红色字体")
