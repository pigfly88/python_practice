for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")
    print();

i=1000

if i>1:
    print(333)
elif i<100:
    print(666)
else:
    print(111)

#print("what's your name?")
'''
name = input();
#print("your name is ", name)
'''



def sayHello():
    print('Hello Python!')

sayHello()

a = [0 for i in range(0,5)]
print(a)