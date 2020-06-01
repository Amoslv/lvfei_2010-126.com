# 9*9乘法表
for index in range(1, 10):
    for position in range(1, index +1):
        print('%d*%d=%2d' % (index, position, index * position), end=' ')
    print(' ')

