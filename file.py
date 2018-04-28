# 文件相关操作


# 写文件
# a+ 读写，写追加模式
fo = open('./test.log', 'a+')
fo.write("Hello Python!\n")

# 读文件
# 这里需要移动文件指针到开头，因为执行完上面的代码以后文件指针已经到了最后了
fo.seek(0, 0)
content = fo.read()
print(content)


# 一行一行地读取文件
fo.seek(0, 0)
line = fo.readline()

while line:
    print(line)
    line = fo.readline()

fo.seek(0, 0)
line = fo.next()

while line:
    print(line)

# 关闭文件
fo.close()