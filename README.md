# 元梦之星全自动星宝农场

这是一个用Python写的自动收获元星宝农场的程序（主要用于一小时作物、动物、鱼饵）

该程序主要使用了pyautogui、paddlepaddle、paddleocr库，使用该程序需要拥有一定的编程基础，懒人版后续考虑更新。

本程序在macOS 14.5 (23F79)、14.6 (23G80)上运行正常，Windows请自测。

使用的Python版本为3.12.4

## 注意事项

使用该程序需要开通农场月卡！

使用该程序需要开通农场月卡！

使用该程序需要开通农场月卡！

未开通星宝农场月卡使用该程序将只能钓鱼。

## 前置条件

1. 安装python，安装对应的库，进入letsgo-farm文件夹，在终端中输入如下命令：
   ```shell
   pip3 install -r requirements.txt
   ```
   如果长时间没有安装完成，请换成国内源(任选其一)：
   ```shell
   pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
   ```
   ```shell
   pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
   ```
   ```shell
   pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
   ```
   ```shell
   pip3 install -r requirements.txt -i https://pypi.douban.com/simple/
   ```
   ```shell
   pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
   ```
2. 用浏览器打开[元梦之星-云游戏](https://gamer.qq.com/v2/cloudgame/game/96897)

3. 安装chrome或Eage浏览器，并在浏览器中将[元梦之星-云游戏](https://gamer.qq.com/v2/cloudgame/game/96897)安装到本地。具体方法为打开网址后登陆，在右侧找到创建桌面快捷方式，如图所示：

![image-20240719193556815](images/image-20240719193556815.png)

4. 自行在游戏中截图，替换掉`images/identify/`文件夹中的所有图片
5. 在identify.py中根据自身系统注释掉相应的代码

## 如何使用

1. 打开元梦之星-云游戏-快捷方式
2. 登陆账号进入农场
3. 修改设置：更多、设置、隐私、个人隐私设置、隐身（防止被打扰，导致程序失效）
4. 选择好种植的作物，和鱼饵
5. 运行程序（main.py）

## 更新记录

2024-08-02: 命令窗口改为GUI，修改日志在窗口显示，添加日志文件，修改钓鱼点位。

2024-08-01: 修复鱼塘出现大丰收之后不能钓鱼的问题，修复农场操作按钮识别成牧场的问题。

2024-07-31: 优化钓鱼、优化代码、统一控制台日志，修改渔场为鱼塘

2024-07-30: 整理识图文件夹，优化识图功能，删除walk.py整合myTools.py

2024-07-26: 修复特殊情况下一直提示“不能钓鱼，检测还剩多少时间成熟”的问题，优化钓鱼逻辑，更改图片存储位置，控制台日志新增毫秒，休息时间添加具体到几点

2024-07-25: **修复钓鱼试图失败的问题**

2024-07-24: **添加识别图片、截图功能、自动洒饵、收获渔场功能**

2024-07-19: **修复了有人推开农场主后不能正常收菜的问题**；更改打开程序的逻辑，将点击固定坐标改为打开固定程序；优化了需要配置坐标的问题

2024-07-18: 自动催产收获牧场；自动浇水收获农场

## 后续计划

在窗口中添加截图功能，截图功能可以自行替换掉需要识别的图片。

增加识别农场和牧场的功能（目前只识别鱼塘）