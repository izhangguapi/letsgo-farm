import os, json, win32com.client


# 检查D盘是否存在
def check_d_drive():
    return os.path.exists("D:\\")


# 写入json
def write_json(path, data):
    with open(path, "w+", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# 创建快捷方式
def create_shortcut(path, target, arguments=[], work_dir="", icon=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(path)
    shortcut.Targetpath = target
    for arg in arguments:
        shortcut.Arguments += " " + arg
    shortcut.WorkingDirectory = work_dir
    shortcut.IconLocation = icon
    shortcut.Save()


if __name__ == "__main__":
    user_data_dir = None
    current_path = os.path.dirname(os.path.abspath(__file__))

    if check_d_drive():
        user_data_dir = "D:\\LetsgoData\\ymzx"
    else:
        user_data_dir = "C:\\LetsgoData\\ymzx"

    num = int(input("请输入多开的数量："))
    data = {"path": user_data_dir, "num": num}

    print("写入json文件")
    data_path = os.path.join(current_path, "data.json")
    write_json(data_path, data)

    for i in range(num):
        i = str(i + 1)
        # 创建快捷方式
        user_data = '--user-data-dir="' + user_data_dir + i + '"'
        shortcut_path = os.path.join(
            os.path.expanduser("~"), "Desktop", "元梦之星" + i + ".lnk"
        )
        target = (
            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge_proxy.exe"
        )
        arguments = [
            "--disable-gpu",
            user_data,
            "--app=https://gamer.qq.com/v2/game/96897",
        ]
        work_dir = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"
        icon = os.path.join(current_path, "icon.ico")
        create_shortcut(shortcut_path, target, arguments, work_dir, icon)
    print("快捷方式创建完成，请前往桌面查看！")
