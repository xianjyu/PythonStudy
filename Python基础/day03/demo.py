# count = 1
# while count < 4:
#     num = int(input('请输入一个数字：'))
#     if num > 66:
#         print('输入的数字大了')
#     elif num < 66:
#         print('输入的数字小了')
#     else:
#         print('恭喜你猜对了')
#         break
#     count += 1
# else:
#     print('次数已达到三次')


# count = 1
# while count < 11:
#     print(count)
#     count += 1


# count = 1
# sum = 0
# while count < 99:
#     if count % 2 == 0:
#         sum = sum - count
#     else:
#         sum += count
#     count += 1
# print(sum)

# s = ''
# print(bool(s))
# s = ' '
# print(bool(s))

# s = 'python全栈22期'

# print(s[6:11])
# print(s[:5:2])
# print(s[:5])


# 有字符串： s = '123a4b5c'
# a.通过对s切片形成新的字符串s = '123'
# b.通过对s切片形成新的字符串s = 'a4b'
# c.通过对s切片形成新的字符串s = '1345'
# d.通过对s切片形成新的字符串s = '2ab'
# e.通过对s切片形成新的字符串s = 'c'
# f.通过对s切片形成新的字符串s = 'ba2'


# s = '123a4b5c'
#
# print(s[:3])    # '123'
# print(s[3:6])   # 'a4b'
# print(s[:7:2])    # '1345'
# print(s[1:6:2])     # '2ab'
# print(s[-1])     # 'c'
# print(s[7])
# print(s[-3:-8:-2])      # 'ba2'
# print(s[-8:-3:-2])      # 错误的语法

# s = 'yuxj'
# print(s.startswith('u', 1, 3))

# print(s[-4:-2])
# print(s.endswith('u', -4, -3))


# s = 'yuxj很nb，yuxj是男性，yuxj长得很帅'
# print(s.replace('yuxj', 'YUXJ'))
# print(s.replace('yuxj', 'YUXJ', 1))
# print(s.replace('yuxj', 'YUXJ', 2))
# print(s.replace('yuxj', 'YUXJ', 1, 3))  # TypeError: replace expected at most 3 arguments, got 4


# s = '  \n学习\t '
# print(s.strip())
# print(s.rstrip())
# print(s.lstrip())
# s = '你abcdef好'
# s2 = s.strip('你好')  # 取出指定的字符：abcdef，只要头尾包含有指定字符序列中的字符就删除
# print(s2)

# s = ':a:b:c'
# print(s.split(':'))
# print(s.split(':', 2))  # ['', 'a', 'b:c']

# s = ['a', 'b', 'c']
# print(':'.join(s))  # a:b:c
# s = ['a', 'b', 1]
# print(':'.join(s))  # TypeError: sequence item 2: expected str instance, int found

# msg = '我叫{}，今年{}，性别{}'.format('yuxj', 25, '男')
# print(msg)
# msg = '我叫{0}，今年{1}，性别{2}，我依然叫{0}'.format('yuxj', 25, '男')
# print(msg)
# msg = '我叫{name}，今年{age}，性别{sex}'.format(age=25, name='yuxj', sex='男')
# print(msg)

# msg = '123abc456'
# print(msg.isalnum())
#
# msg = 'abcde1f'
# print(msg.isalpha())

# msg = input('请输入数字：')
# if msg.isdecimal():
#     print(int(msg))
# else:
#     print('输入有误')

# s = 'yuxj'
# index = 0
# while index < 4:
#     print(s[index])
#     index += 1


# s = 'yuxj'
# for i in s:
#     print(i)
#     if i == 'x':
#         break

# s = 'yuxj'
# for i in s:
#     print(i)
#     if i == 'x':
#         continue


# count = 1
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(6)


# msg = 'yuxj'
#
# for i in msg:
#     if i == 'x':
#         break
#     print(i)
# else:
#     print('……')
