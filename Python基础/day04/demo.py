# s = 'yuxj'
# print(s[0])
# print(s[-1:-3:-1])
# print(s[-1])

# 使用for循环对s='asdfer'进行循环，但是每次打印的内容都是'asdfer'

# s = 'asdfer'
# count = 0
# for i in s:
#     print('第' + str(count) + '次循环，', s)
#     count += 1

# 使用for循环对s='asdfer'进行循环，但是每次打印的内容都加上sb,例如asb,ssb

# s = 'asdfer'
# for i in s:
#     print(i + 'sb')

# 使用for循环对s= '321'进行循环，打印的内容依次是'倒计时3秒'，'倒计时2秒'，'倒计时1秒'，出发
# s = '321'
# count = 0
# for i in s:
#     print('倒计时{}秒'.format(3-count))
#     count += 1
# else:
#     print('出发')


# 实现一个整数加法计算器(两个数相加)
# num1 = input('请输入第一个数字：')
# num2 = input('请输入第二个数字：')
#
# if num1.isdigit() and num2.isdigit():
#     sum = int(num1) + int(num2)
#     print(sum)
# else:
#     print('输入的不是数字')

# 如content=input('请输入内容：') 用户输入5+9或5+ 9或5 + 9，然后进行分割再计算

# content = input('请输入内容：').strip()
# split_content = content.split('+')
# sum = 0
# for i in split_content:
#     sum += int(i)
# print(sum)














# l = [100, '太白', True, [1, 2, 3]]
#
# print(l[0], type(l[0]))
# print(l[1], type(l[1]))
# print(l[2], type(l[2]))
# print(l[3], type(l[3]))

# l = [1, 3, 2, 'a', 4, 'b', 5, 'c']
# # 通过l列表的切片形成形成新的列表，l=[1,3,2]    顾头不顾腚
# print(l[:3])
# # 通过l列表的切片形成形成新的列表，l=['a', 4, 'b']
# print(l[3:6])
# # 通过l列表的切片形成形成新的列表，l=[3, 'a', 'b']
# print(l[1:6:2])
# # 通过l列表的切片形成形成新的列表，l=['b', 'a', 3]
# print(l[-3:-8:-2])

# l = ['太白', 'wc', '女神', 'yxj']
# l.append('abc')
# print(l)

# l = []
# while 1:
#     name = input('请输入姓名：(提示：退出按Q或q)')
#     if name.upper() == 'Q':
#         break
#     l.append(name)
# print(l)

# l = ['太白', 'wc', '女神', 'yxj']
# l.insert(2, 'abc')
# print(l)

# l = ['太白', 'wc', '女神', 'yxj']
# l.extend('abcd')
# print(l)

# l = ['太白', 'wc', '女神', 'yxj']
# l.extend(['yuxj'])
# print(l)

# l = ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
# l.pop()
# print(l)


# l = ['a', 'b', '太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
# l.remove('a')
# print(l)


# l = ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
# l.clear()
# print(l)

# l = ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
#
# del l[1]
# print(l)    # ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']

# l = ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
# del l[::2]
# print(l)    # ['wc', 'yxj', 'b', 'd']

# l = ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
# l[0] = 'abcd'
# print(l)

# l = ['太白', 'wc', '女神', 'yxj', 'a', 'b', 'c', 'd']
# l[3:] = 'python'
# print(l)

# l = ['太白', 'wc', '女神', 'yxj', '大神']
# l[::2] = 'abc'  # 太白=a  女神=b  yxj=c
# print(l)    # ['a', 'wc', 'b', 'yxj', 'c']

# l = ['太白', 'wc', '女神', 'yxj', '大神']
# for i in l:
#     # print(i)    # 太白    wc  女神  yxj 大神

# l = ['alex', 'WuSir', 'RiTian', 'Barry', 'WenZhou']
# l2 = [1, 'a', 3, 4, 'b']
#
# l.extend(l2)
# print(l)


# l = ['alex', 'WuSir', 'RiTian', 'Barry', 'WenZhou']
# s = 'qwert'
# l.extend(s)
# print(l

# l = ['alex', 'WuSir', 'RiTian', 'Barry', 'WenZhou']
# l.pop(1)
# l.remove('RiTian')
# del l[2]
# del l[1:4]
# print(l)

# l = [1, 2, 'taibai', [1, 'alex', 3]]

# l[1] = 'TAIBAI'
# print(l)

# l[3].append('老男孩教育')
# l[3].insert(3, '老男孩教育')
# l[3].extend(['老男孩教育'])

# l[3][1] += 'sb'
# print(l)

# a, b = (1, 2)
# print(a, b)

# for i in range(10):
#     print(i)    # 0-9，顾头不顾腚
#
# for i in range(2, 11, 2):
#     print(i)
#
# for i in range(10, 0 , -2):
#     print(i)

# l = [1, 2, 3, 'alex', 'yuxj']
# count = 0
# for i in l:
#     print(count)
#     count += 1
#
# for i in range(len(l)):
#     print(i)


# msg = input('请输入你的内容：')
# count = 0
#
# for i in msg:
#     if i.isdigit():
#         count += 1
# print(count)

# msg = input('请输入内容：')
# if msg == msg[::-1]:
#     print(msg + '是回文')
# else:
#     print(msg + '不是回文')

# for i in range(2, 11, 2):
#     print(i)

for i in range(10, 0, -2):
    print(i)

