a = input('First number:')
b = input('Second number:')

try:
    answer = int(a) / int(b)
except ZeroDivisionError:
    print("You can't devide by 0")
else:
    print(answer)