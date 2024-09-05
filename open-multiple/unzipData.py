import os, zipfile


# 检查D盘是否存在
def check_d_drive():
    return os.path.exists("D:\\")


def unzip(zip_path, file_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(file_path)


if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    if check_d_drive():
        user_data_dir = "D:\\LetsgoData\\ymzx"
    else:
        user_data_dir = "C:\\LetsgoData\\ymzx"

    print("正在解压到文件...")
    zip_path = os.path.join(current_path, "LetsgoData.zip")
    unzip(zip_path, user_data_dir + "1")
    print("解压完成！")
