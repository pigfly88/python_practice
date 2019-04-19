numbers = [1, 2, 3, 4, 5]
print(len(numbers))

print(numbers[0])

numbers.append(6)
print(numbers[-1])

numbers[1] = 99
print(numbers)

numbers.insert(1,666)
print(numbers)

del numbers[3]
print(numbers)

elem = numbers.pop(1)
print(numbers, elem)

numbers.remove(4)
print(numbers)

print(sorted(numbers))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

for number in numbers:
    print(number)

# 数字集
for num in range(1,6):
    print(num)

# 使用list将转换为列表
nums2 = list(range(1,6))
print(nums2)

nums11=[]
nums = range(1,11)
for num in nums:
    nums11.append(num**2);
print(nums11);

nums3 = [value**2 for value in range(1,11)]
print(nums3)

# 切片
print(nums3[0:3])

# 复制
nums4 = nums3[:] # 如果不加冒号相等于引用


nums3.append(123)
print(nums3, nums4)

# 元组
friends = ('tim', 'tom')
# 报错，元组不允许改变值
#friends[1] = 'pigfly'
