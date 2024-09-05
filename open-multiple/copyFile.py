import shutil, json, os


# 读取json
def read_json():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    data = read_json()
    path = data["path"]
    num = data["num"]

    for i in range(num - 1):
        folder_path = path + str(i + 2)
        if os.path.exists(folder_path):
            print("文件夹存在")
        else:
            print(f"复制第{i + 1}份文件...", path + "1", folder_path)
            shutil.copytree(path + "1", folder_path)

    print("完成")
