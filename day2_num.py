# 判断逻辑 and、or、not/优先级  not>and>or

# //=是取整赋值运算符；%=是取余赋值运算符

# 找出水仙花数
# 153 = 1*1*1 + 5*5*5 + 3*3*3

for number in range (100, 1000):
    hund = int(number/100)
    temp = number - 100 * hund
    ten = int(temp/10) 
    indiv = temp - ten * 10
    total = hund ** 3 + ten ** 3 + indiv ** 3
    if number == total:
        print(number)

print('第二种方式查找')

for number in range (100, 1000):
    hund = number // 100
    indiv = number % 10
    ten = (number - 100 * hund) //10
    total = hund ** 3 + ten ** 3 + indiv ** 3
    if number == total:
        print(number)

# 判断一个数是否为水仙花数
all = True
while all:
    inputStr = input('请输入100-1000之间的任意一个三位数')

    inputNum = 0
    try:
        inputNum = int(inputStr)
        if inputNum < 100:
            print('请输入大于100的三位数')
        elif inputNum >= 1000:
            print('请输入小于1000的三位数')
        else:
            hund = inputNum // 100
            indiv = inputNum % 10
            ten = (inputNum - 100 * hund) //10
            total = hund ** 3 + ten ** 3 + indiv ** 3
            if inputNum == total:
                print('%d是水仙花数' % inputNum)
                all = False
            else:
                print('%d不是水仙花数' % inputNum)
    except ValueError:
        print('请输入正确的数字')