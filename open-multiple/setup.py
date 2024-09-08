import cefpython3
import subprocess
import os
import shutil

class PyinstallerCompile:

    _pyRelOnPath = None
    _relyOnDir  = []
    _relyOnFile = []

    _distPath    = os.path.join(os.getcwd(),'dist')

    def __init__(self,ScriptName):
        self.no_suffix_script_name = ScriptName
        self.script_file = os.path.join(os.getcwd(), "{}.py".format(ScriptName))
        self.delete_before_generates()

    def setDistPath(self,path):
        self._distPath = path

    def setRelyOnDirPath(self,path):
        self._relyOnDir.append(path)

    # def setRelyOnFilePath(self,path):
    #     self._relyOnFile.append(path)

    def setPyRelOnPath(self,path):
        self._pyRelOnPath = path

    def delete_before_generates(self):
        """删除之前打包生成的文件"""
        print("*******正在删除之前打包的生成文件....")
        try:
            shutil.rmtree(self._distPath)
            shutil.rmtree(os.path.join(os.getcwd(),'build'))
            os.remove("{}.spec".format(self.no_suffix_script_name))
        except Exception as e:
            pass
        print("*******删除成功！")

    def script_to_exe(self):
        # 相当于执行打包命令： Pyinstaller MainUi.py
        print("*******开始打包cefpython3应用：", self.script_file)

        subprocess.run("Pyinstaller -p {} -w --distpath={} --icon=icon.ico -D --hidden-import=inspect --hidden-import=json {}".format(
            self._pyRelOnPath,
            self._distPath,
            self.script_file))

    def copytree(self, src, dst, ignores_suffix_list=None):
        print("********正在复制将{}目录下的文件复制到{}文件夹下....".format(src, dst))
        os.makedirs(dst, exist_ok=True)
        names = [os.path.join(src, name) for name in os.listdir(src)]
        for name in names:
            exclude = False
            for suffix in ignores_suffix_list:
                if name.endswith(suffix):
                    exclude = True
                    continue
            if not exclude:
                if os.path.isdir(name):
                    new_dst = os.path.join(dst, os.path.basename(name))
                    shutil.copytree(name, new_dst, ignore=shutil.ignore_patterns(*ignores_suffix_list))
                else:
                    shutil.copy(name, dst)

    def solve_dependence(self):
        print("*******解决依赖：复制依赖文件到执行文件的目录下....")
        _dst = "{}/{}".format(self._distPath,self.no_suffix_script_name)
        for path in self._relyOnDir:
            if type(path) == dict:
                if not 'suffix' in path:
                    path['suffix'] = []
                self.copytree(path['path'], _dst + '/{}'.format(
                    os.path.basename(path['path'])
                ), path['suffix'])
            else:
                self.copytree(path, _dst, [".txt", ".py", ".log", "examples", ".pyd", "__"])

        # for path in self._relyOnFile:
        #     print("********正在复制将{}文件复制到{}文件夹下....".format(path, _dst))
        #     if type(path) == dict:
        #         shutil.copy(path['path'],_dst)
        #         if 'fun' in path:
        #             path['fun']()
        #     else:
        #         shutil.copy(path,_dst)

    def exec_application(self):
        print("*******执行成功打包的应用....")
        exePath = os.path.join(self._distPath,self.no_suffix_script_name,'{}.exe'.format(self.no_suffix_script_name))
        print("启动文件所在位置：{}".format(exePath))
        subprocess.run(exePath)

    def run(self):
        self.delete_before_generates()
        self.script_to_exe()
        self.solve_dependence()
        self.exec_application()
      
rootPath = os.getcwd()
compile = PyinstallerCompile('openMultiple')

# 设置PY环境扩展包查找目录
compile.setPyRelOnPath(os.path.join(rootPath,'EnvService','Lib','site-packages'))

# 设置存储编译目录路径
compile.setDistPath(os.path.join(rootPath,'exe'))

# 依赖文件
# filePath = [
#     os.path.join(rootPath,'config.ini')
# ]
# for path in filePath:
#     compile.setRelyOnFilePath(path)

# 依赖目录
dirPath = [
    os.path.dirname(cefpython3.__file__),
]
for path in dirPath:
    compile.setRelyOnDirPath(path)

compile.run()
