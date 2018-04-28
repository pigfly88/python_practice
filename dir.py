# 目录相关
import os

# 当前目录
print(os.getcwd())

# 切换目录
os.chdir('D:\web')

print(os.getcwd())

# 列出文件夹下的所有文件
with os.scandir() as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
