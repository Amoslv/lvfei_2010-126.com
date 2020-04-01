inputNum = input('请输入一个数字')

inputNum2 = 1000 - int(inputNum)
inputNum2 = inputNum2 * 30

if inputNum2 > 3000:
    print('运算结果大于3000')
else:
    print('运算结果小于3000')