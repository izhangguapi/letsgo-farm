from cefpython3 import cefpython as cef
import sys

# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
# sys.excepthook = cef.ExceptHook

# 创建浏览器
cef.Initialize()


browser = cef.CreateBrowserSync(
    url="https://gamer.qq.com/v2/game/96897",
    window_title="元梦之星"
)

# browser.SetBounds(0, 0, 100, 600)  # 设置浏览器窗口的大小为宽1000，高600

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()

# import webview


# webview.create_window('元梦之星', 'https://gamer.qq.com/v2/game/96897',width=1000, height=600)
# webview.start()