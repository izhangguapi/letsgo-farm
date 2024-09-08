from cefpython3 import cefpython as cef
import sys

def main():
    # 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
    sys.excepthook = cef.ExceptHook  

    # 创建浏览器
    cef.Initialize()
    cef.CreateBrowserSync(url="https://gamer.qq.com/v2/game/96897", window_title="元梦之星")

    # 消息循环：监听信号和处理事件
    cef.MessageLoop()

    # 结束进程
    cef.Shutdown()

if __name__ == '__main__':
    main()