print('  欢迎来到大数据产业园')

# 定义函数
def indexIsMax(index,maxNumber, sign):
    if index == maxNumber:
        print(sign)
    else:
        print(sign, end="")
    return


# 起始的横线
mMaxNumber = 25
for index in range(0,mMaxNumber):
    indexIsMax(index,mMaxNumber, '=')

print("")

for index in range(mMaxNumber):
    indexIsMax(index, mMaxNumber,'-')
print('')

