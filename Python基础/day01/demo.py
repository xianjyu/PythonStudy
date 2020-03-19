content = 'I am yuxj, 18 year old'
content2 = "I'm yuxj, 18 year old"
content3 = '''
每想你一次，
天上飘落一粒沙，
从此形成了撒哈拉。
每想你一次，
天上就掉下一滴水，
于是形成了太平洋。
        - 三毛
'''

# print(content)
# print(content2)
# print(content3)
#
#
# str1 = 'yu'
# str2 = 'xianjia'
# print(str1 + str2)
#
# str3 = '坚强'
# print(str3 * 5)


# name = input('请输入姓名：')
# age = input('请输入年龄：')
# sex = input('请输入性别：')
# msg = '我叫' + name + ', 今年' + age + ', 性别' + sex
# print(msg)


# age = input("请输入你的年龄：")
#
# if age > 18:    # age是字符串类型
#     print('恭喜你，成年了')    # TypeError:类型错误
# else:
#     print('小屁孩')

# age = input("请输入你的年龄：")
#
# if int(age) > 18:    # age是字符串类型
#     print('恭喜你，成年了')    # TypeError:类型错误
# else:
#     print('小屁孩')


username = input('请输入用户名：')
password = input('请输入密码：')
you_code = input('请输入验证码：')

code = 'qwer'

if you_code == code:
    if username == 'yuxj' and password == 'yuxj':
        print('登录成功')
else:
    print('验证码错误')


