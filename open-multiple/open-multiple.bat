chcp 65001
@echo off
echo 菜单:
echo 1.创建快捷方式
echo 2.解压数据
echo 3.复制文件

set /p num=请选择:

if %num%==1 (
    python createShortcut.py

)else if %num%==2 (
    python unzipData.py

)else if %num%==3 (
    python copyFile.py
)

pause