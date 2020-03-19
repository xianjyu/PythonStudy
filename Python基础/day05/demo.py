# l = range(5)
# print(l[1:3])


# for i in range(1, 5, -1):
#     print(i)    # 没有值，要5写在前面，1写在后面
# for i in range(5, 1, -1): # 倒序
#     print(i)


# dict = {'太白': {'name': '太白金星', 'age': 17, 'sex': '男'},
#         '22期': ['a', 'b', 'v']}

# dic = dict((('one', 1), ('two', 2), ('three', 3)))
# print(dic)

# dic = dict(one=1, two=2, three=3)
# print(dic)

# dic = dict({'one': 1, 'two': 2, 'three': 3})
# print(dic)

# dic = {[1, 2, 3]: 'alex', 1: 666}
# print(dic)

# dic = {1: 'alex', 1: 'yuxj', 2: 'abc'}
# print(dic)

# dic = {'name': 'yuxj', 'age': 17}
# ret = dic.pop('hobby', '没有这个键')
# print(ret)

# lat = {"六月": ["飞", "雪"], "七月": "99", "八月": "炎阳"}
# lat_1 = {"六月": "寒冬", "七月": "冬去", "三月": "春来"}
# lat_1.update(lat)
# print(lat_1)

# 简介修改字典中的键
# dict = {'a': 1, 'b': 2}
#
# dict["c"] = dict.pop("a")
# print(dict)

# a = {'age': 18, 'name': 'gaoqi', 'job': 'techer'}
# b = {'top': 173, 'name': 'Vince', 'tel': 123456}
# a.update(b)
# print(a)
# dic = {'name': 'yuxj', 'age': 17}
# # print(dic['hobby'])     # KeyError: 'hobby'
# print(dic.get('hobby')) # None
# ret = dic.get('hobby', '此键没有对应的值')
# print(ret)  # 此键没有对应的值

# dic = {'name': 'yuxj', 'age': 17}
# print(dic.keys(), type(dic.keys()))     # dict_keys(['name', 'age']) <class 'dict_keys'>
# print(list(dic.keys()))
# for i in dic.keys():
#     print(i)
# print(dic.values(), type(dic.values()))
# print(list(dic.values()))
# for i in dic.values():
#     print(i)
# print(dic.items())
# for i in dic.items():
#     print(i)

# for key, value in dic.items():
#     print(key, value)
# dic = {'k1': 'v1', 'ke': 'v2', 'k3': [11, 22, 33]}
# 请在字典中添加一个键值对，'k4':'v4'，输出添加后的字典
# dic['k4'] = 'v4'   # 直接增加
# dic.setdefault('k4', 'v4')
# print(dic)

# dic['k1'] = 'yuxj'
# print(dic)

# dic['k3'].append('44')
# dic['k3'].insert(3, '44')
# dic['k3'].extend(['44'])
# print(dic)

# dic['k3'].insert(1, '44')
# print(dic)


# dic = {'name': '汪峰',
#        'age': 48,
#        'wife': [{'name': '国际章', 'age': 38}],
#        'children': {'girl_first': '小苹果', 'girl_second': 'xiaoyi', 'girl_three': 'dingding'}}


# print(dic.get('name'))
# for dic2 in dic.get('wife'):

#     print(dic2.get('name'))i

# for i in dic.get('children').values():
#     print(i)

