# 将random模块导入
import random

fruit_name = ""
# [fruit_name] * 数字，该形式是将列表项重复若干遍。比如执行 ['X'] * 3 将得到 ['X', 'X', 'X']；
def harvest():
    return [fruit_name] * random.randint(1, 9)