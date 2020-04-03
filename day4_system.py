# 根据业务需求，开发一个货币兑换的服务系统，具体要求如下：
# （1）实现人民币兑换美元的功能
# （2）实现美元兑换人民币的功能
# （3）实现人民币兑换欧元的功能

def printSymbol(num, symBol, printSpace):
    if printSpace:
        print('')
    else:
        for index in range(num):
            print(symBol, end='')

choose = '-1'
dict = {1:'人民币转换美元', 2:'美元转换人民币', 3:'人民币转换欧元', 0:'结束程序'}
print(dict)
for value in dict:
    print(value, end=': ')
    print(dict[value])
# inputChoose = input('请选择货币转换的, 输入 0, 1, 2, 3...')

# try:
#     choose = int(choose)
# except ValueError:
#     print('输入的数字有问题')

time = 0
while time < 1:
    # 输入转换的数字
    inputMoney = input('请输入需要转换的数额\n')

    money = 0
    try:
        money = int(inputMoney)
        time = 1
        # 开始进行打印
        maxNum = 10
        printSymbol(maxNum, '*', False)
        print('欢迎使用货币转换服务系统', end='')
        printSymbol(maxNum, '*', False)
        print('')

        # 人民币转换
        print(1, end=' . ')
        print(dict[1])
        print('欢迎使用人民币转换美元服务')
        print('您需要转换的人民币为: {} 元'.format(money))
        doller = money / 7.14
        print('兑换成美元为: {} $'.format(doller))
        printSymbol(3 * maxNum, '=', True)

        # 美元转换人民币
        print(2, end=' . ')
        print(dict[2])
        print('欢迎使用美元转换人民币服务')
        print('您需要转换的美元为: {} $'.format(money))
        doller = money * 7.14
        print('兑换成人民币为: {} 元'.format(doller))
        printSymbol(3 * maxNum, '=', True)

        # 人民币转换欧元
        print(3, end=' . ')
        print(dict[3])
        print('欢迎使用人民币转换欧元服务')
        print('您需要转换的人民币为: {} 元'.format(money))
        doller = money * 0.12
        print('兑换成欧元为: {} €'.format(doller))
        printSymbol(3 * maxNum, '=', True)

        # 结束程序
        print(0, end=' . ')
        print(dict[0])
        print('感谢您的使用， 祝您生活愉快， 再见！')
        printSymbol(3 * maxNum, '=', True)
    except ValueError:
        if time < 9:
            print('请输入正确的数字!!!')
        else:
            print('即将退出货币转换系统...')
        time = time + 1