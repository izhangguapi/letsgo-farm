import selectWindow, threading, win32gui, datetime
import tkinter as tk
from tkinter import ttk
import myTools as mt
import letsgoFarm as lgf


def open_select_window():
    selectWindow.create_window()
    window.wait_window(selectWindow.window)
    # if mt.title != None:
    #     window.title(mt.title + " - " + str(mt.hwnd))
    # print("窗口关闭")
    try:
        title = mt.title + " - " + str(mt.hwnd)
        window.title(title)
        game_rect = win32gui.GetWindowRect(mt.hwnd)
        this_window = win32gui.FindWindowEx(0, 0, None, title)
        x = game_rect[0]
        y = game_rect[1] + 592
        win32gui.MoveWindow(this_window, x, y, 0, 0, True)
        mt.log_name = (
            str(datetime.datetime.now().strftime("%Y年%m月%d日_%H时%M分%S秒"))
            + mt.title
            + "_"
            + str(mt.hwnd)
            + ".txt"
        )
    except:
        pass


def run_letsgoFarm():
    """开始挂机"""
    run.config(state=tk.DISABLED)
    select.config(state=tk.DISABLED)
    mt.exit_event.clear()
    thread = threading.Thread(target=lgf.start)
    thread.daemon = True
    thread.start()
    stop.config(state=tk.NORMAL)


def stop_letsgoFarm():
    """停止挂机"""
    run.config(state=tk.NORMAL)
    select.config(state=tk.NORMAL)
    mt.exit_event.set()
    stop.config(state=tk.DISABLED)


def test_1():
    # print(mt.lgf_config)
    x = mt.position["socialize"]["x"]
    y = mt.position["socialize"]["y"]
    mt.vkb.mouse_move_press(x=x, y=y)


def test_2():
    cw = mt.ControlWindow(mt.hwnd)
    cw.screenshot_window()


# def on_click(event):
#     window.focus_get()


# 创建标签框架（农牧鱼）
class CreateLF:
    enable = None
    timer = None
    h = "00"
    m = "00"
    s = "00"

    def __init__(self, window):
        self.enable = tk.BooleanVar(value=True)
        self.timer = tk.BooleanVar()

    def on_mouse_leave(self, event):
        window.focus_set()

    def focus_out(self, event):
        num = event.widget.get().strip()
        name = event.widget.winfo_name()

        if len(num) > 2 or not num.isdigit():
            event.widget.delete(0, tk.END)
            return
        if len(num) == 1:
            num = "0" + num
        if name == "h":
            if int(num) > 23:
                event.widget.delete(0, tk.END)
                num = "00"
            self.h = num
        elif name == "m":
            if int(num) > 59:
                event.widget.delete(0, tk.END)
                num = "00"
            self.m = num
        elif name == "s":
            if int(num) > 59:
                event.widget.delete(0, tk.END)
                num = "00"
            self.s = num

        # 获取LabelFrame名称
        lf_name = str(event.widget.master).split(".")[-1]
        today = str(datetime.date.today())
        time = self.h + ":" + self.m + ":" + self.s
        if lf_name == "农场":
            mt.lgf_config["farm_time"] = today + " " + time
        elif lf_name == "牧场":
            mt.lgf_config["pasture_time"] = today + " " + time
        elif lf_name == "鱼塘":
            mt.lgf_config["fishpond_time"] = today + " " + time
        else:
            mt.lgf_config["prayers_time"] = today + " " + time

    def focus_out_text(self, event):
        text = event.widget
        content = text.get("1.0", "end-1c")  # 获取Text组件的内容
        lines = content.split("\n")  # 将内容按行分割
        # print(lines)
        if len(lines) > 3:
            text.delete("3.10", "end-1c")

        for i in range(1, len(lines)):
            text.delete(str(i) + ".10", str(i) + ".end")
        list_uid = text.get("1.0", "end-1c").split("\n")
        mt.lgf_config["prayers_uid"] = list_uid

    def get_checkbtn(self, event):
        lf_name = str(event.widget.master).split(".")[-1]
        if lf_name == "农场":
            mt.lgf_config["farm_enable"] = self.enable.get()
            mt.lgf_config["farm_timer"] = self.timer.get()
        elif lf_name == "牧场":
            mt.lgf_config["pasture_enable"] = self.enable.get()
            mt.lgf_config["pasture_timer"] = self.timer.get()
        elif lf_name == "鱼塘":
            mt.lgf_config["fishpond_enable"] = self.enable.get()
            mt.lgf_config["fishpond_timer"] = self.timer.get()
        else:
            mt.lgf_config["prayers_enable"] = self.enable.get()

        # print(mt.lgf_config)
        # if self.enable_v:
        #     print("启用")
        # if self.timer_v:
        #     print("定时")
        # pass

    def create(
        self,
        title,
        col,
        is_enable=True,
        enable_text="启用",
        is_timer=True,
        timer_text="定时关闭",
        is_text=False,
        rowspan=1,
    ):
        self.lf = tk.LabelFrame(window, text=title, name=title)
        # self.lf.grid(row=0, column=col, padx=px, pady=5)
        self.lf.grid(row=0, column=col, rowspan=rowspan, sticky="nsew")
        row = 0
        if is_enable:
            enable = tk.Checkbutton(
                self.lf,
                text=enable_text,
                variable=self.enable,
            )
            enable.grid(row=row, column=0, columnspan=5)
            enable.bind("<Leave>", self.get_checkbtn)
            row += 1

        if is_timer:
            timer = tk.Checkbutton(self.lf, text=timer_text, variable=self.timer)
            timer.grid(row=row, column=0, columnspan=5)
            timer.bind("<Leave>", self.get_checkbtn)
            row += 1

        h = tk.Entry(self.lf, width=2, name="h")
        h.grid(row=row, column=0)
        h.bind("<FocusOut>", self.focus_out)
        h.bind("<Leave>", self.on_mouse_leave)

        lbhm = tk.Label(self.lf, text=":")
        lbhm.grid(row=row, column=1)

        m = tk.Entry(self.lf, width=2, name="m")
        m.grid(row=row, column=2)
        m.bind("<FocusOut>", self.focus_out)
        m.bind("<Leave>", self.on_mouse_leave)

        lbms = tk.Label(self.lf, text=":")
        lbms.grid(row=row, column=3)

        s = tk.Entry(self.lf, width=2, name="s")
        s.grid(row=row, column=4)
        s.bind("<FocusOut>", self.focus_out)
        s.bind("<Leave>", self.on_mouse_leave)

        row += 1

        if is_text:
            prayers_text = tk.Text(self.lf, height=5, width=11, state=tk.DISABLED)
            prayers_text.grid(row=row, column=0, columnspan=5)
            prayers_text.bind("<FocusOut>", self.focus_out_text)
            prayers_text.bind("<Leave>", self.on_mouse_leave)


def create_other_lf():
    global select, run, stop
    other = tk.LabelFrame(window, text="其他")
    other.grid(row=0, column=4, rowspan=2, sticky="nsew")

    select = tk.Button(other, text="选择窗口")
    select.config(command=open_select_window)
    select.grid(row=0, column=0)
    run = tk.Button(other, text="开始运行")
    run.config(command=run_letsgoFarm)
    run.grid(row=0, column=1)
    # 寻找窗口
    test = tk.Button(other, text="测试按钮")
    # test.config(command=mt.check_settings)
    test.grid(row=1, column=0)
    stop = tk.Button(other, text="停止程序")
    stop.config(command=stop_letsgoFarm, state=tk.DISABLED)
    stop.grid(row=1, column=1)

    quit = tk.Button(other, text="退出程序")
    quit.grid(row=2, column=0, columnspan=2, sticky="nsew")
    quit.config(command=window.quit)


def focus_out(event):
    mt.lgf_config["loop_s"] = int(event.widget.get())


def creat():
    global window
    window = tk.Tk()
    window.title("请选择游戏窗口")

    fram = CreateLF(window)
    fram.create("农场", 0)
    pasture = CreateLF(window)
    pasture.create("牧场", 1)
    fishpond = CreateLF(window)
    fishpond.create("鱼塘", 2)
    # prayers = CreateLF(window)
    # prayers.create("祈愿", 3, is_enable=False, is_text=True, rowspan=2)

    settings_lf = tk.LabelFrame(window, text="设置", name="设置")
    settings_lf.grid(row=0, column=3, sticky="nsew")
    loop_s = tk.Entry(settings_lf, width=3)
    loop_s.insert(0, "530")
    loop_s.grid(row=0, column=0)
    loop_s.bind("<FocusOut>", focus_out)
    l = tk.Label(settings_lf, text="秒执行一次")
    l.grid(row=0, column=1, columnspan=3)

    create_other_lf()

    mt.create_listbox(window)

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    creat()
