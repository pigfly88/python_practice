def sayHello(name='someone', age=18):
    print('Hello ' + name + ', your age is ' + str(age))

sayHello('pigfly')
sayHello(age=31)

def sayGoodbye(*messages, **items):
    print(messages[0] + messages[1] + items['price1'] + items['price2'])

sayGoodbye(1, 2, price1=9.9, price2=19.9)