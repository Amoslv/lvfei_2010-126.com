# 列表 

list = []
list.append('Python')
list.append('Java')
list.append('PHP')

# 打印索引值
print(list[0])
print(list)

#从索引0开始，打印到索引2的值，不包含索引2
print(list[0:2])

# 删除某个值
list.pop(0)
print(list)

# 插入某个数据
list.insert(1, 'Python')
print(list)

print('-----------下面打印的是字典-----------')
# 字典
dict = {'apple': 5, 'pear': 3, 'orange': 6}

print(dict)
# 打印某个对应的key值
print(dict['apple'])

# 更新数据
dict['apple'] = 10
print(dict['apple'])

# dict['mango'] = 20若字典中有class则会对原值进行修改，若没有则在原字典的基础上新增key并对其赋值
dict['mango'] = 20
print(dict)

# 删除数据
dict.pop('apple')
print(dict)
