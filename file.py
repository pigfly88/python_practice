'''
文件相关操作

mode:
    r: 读（默认）
    w: 覆盖写
    a: 追加写
    x: 创建，文件存在返回错误
    +: 读写，在以上模式中扩展为读写
'''

# 写文件
fo = open('./test.log', 'a+')
fo.write("Hello Python!\n")


# 读文件
# 这里需要移动文件指针到开头，因为打开文件的模式采用的是追加写，执行完上面的代码以后文件指针已经到了最后了
fo.seek(0, 0)
content = fo.read()
print(content)

# 一行一行地读取文件
fo.seek(0, 0)
line = fo.readline()
i=1
while line:
    print("#%d %s" %(i, line))
    line = fo.readline()
    i+=1

# 文件内容按行生成列表
fo.seek(0, 0)
lines = fo.readlines()
print(lines)

# 关闭文件
fo.close()

