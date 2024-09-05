import webview

 
# 创建多个窗口的函数
def create_multiple_windows(urls, user_data_dirs):
    windows = []
    for i in range(len(urls)):
        window = webview.create_window(
            'Window ' + str(i),
            urls[i],
            
            # user_data_dirs
            # user_data_dirs=user_data_dirs[i]
        )
        windows.append(window)
    return windows
 
# 主函数
def main():
    # 网页URL列表
    urls = ['https://gamer.qq.com/v2/cloudgame/game/96897', 'https://gamer.qq.com/v2/cloudgame/game/96897']
    # 用户数据目录列表
    user_data_dirs = ['/data1', '/data2']
    
    # 创建多个窗口
    windows = create_multiple_windows(urls, user_data_dirs)
    
    # 运行事件循环直到所有窗口关闭
    webview.start(http_server=True)
 
if __name__ == '__main__':
    main()