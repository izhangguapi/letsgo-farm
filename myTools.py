import datetime,time


class ANSI:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[m"


def get_date():
    """获取当前日期和时间"""
    return "[" + str(datetime.datetime.now()) + "] - "


def print_red(text):
    """打印红色文本"""
    print(ANSI.RED + get_date() + text + ANSI.RESET)


def print_green(text):
    """打印绿色文本"""
    print(ANSI.GREEN + get_date() + text + ANSI.RESET)


def print_nol(text):
    print(get_date() + text)


def sleep(seconds):
    """休眠的异常处理"""
    try:
        time.sleep(seconds)
    except:
        print_red("程序被强制退出")
        exit()
