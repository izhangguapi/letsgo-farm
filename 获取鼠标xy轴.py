import tkinter as tk
import pyautogui
 
def on_click(event):
    # 获取鼠标当前位置
    x, y = pyautogui.position()
    # 在文本框中显示鼠标位置
    text_box.insert('end', f'鼠标的坐标为: x={x}, y={y}\n')
 
def clear_text():
    # 清空文本框内容
    text_box.delete('1.0', 'end')
 
root = tk.Tk()
root.title("Mouse Position Tracker")
 
text_box = tk.Text(root, height=5, width=100)
text_box.pack()
 
# 创建一个按钮，用于清除文本框内容
clear_button = tk.Button(root, text='Clear', command=clear_text)
clear_button.pack()
 
# 监听鼠标点击事件
root.bind('<Button-1>', on_click)

root.attributes('-topmost', True)
# 启动事件循环
root.mainloop()