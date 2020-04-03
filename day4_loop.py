# 循环练习

# 计算从1到1000以内所有奇数的和并输出，结果为250000
sum1 = 0
num1 = 1
#循环条件
while num1 < 1000:
    #判断条件
    if(num1 % 2 != 0):
         # 求和
        sum1 = sum1 + num1
    num1 = num1 + 1
print(sum1)

# range() 函数用于创建一个整数列表，为左闭右开，i的值为0；j的值为0、1、2
print('------双层嵌套------')
for i in range(1):
    for j in range(3):
        print('*', end='')

# 打印数值
number = 20
while number < 1000:
    print(number)
    number += 20

# 求1-100的总和
num2 =1
total = 0
while num2 <= 100:
    total += num2
    num2 +=1

print('1到100的总和为 %s' % total)
print('1到100的总和为 {}'.format(total))
