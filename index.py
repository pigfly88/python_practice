# 99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")
    print();

i=1

if i==1:
    print(1)
elif i==2:
    print(2)
else:
    print(3)

# 命令行输入输出
'''
print("what's your name?")
name = input();
print("your name is ", name)
'''

# 函数定义
def sayHello(name='zz', age=30):
    print('Hello Python! My name is %s, My age is %d' %(name, age))

sayHello()

# 列表
a = [1, 2, 3]
print(a)

# 元组 不可更改
t = (1, 2, 3)
print(t)

# 字典
d = {
    'sex':'男',
    'age':21
}
print(d)

t = (1, 2, a, d)
t[2][0] = 0
print(t)

# 集合（去重）
s = set('ababcdede')
print(s)

s = set([1,2,2,3])
print(s)