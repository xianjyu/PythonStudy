> ## 1.Python基础数据类型
在编程语言中都会有一个叫数据类型的东东，其实就是对常用的各种数据类型进行了明确的划分，意思就是你想让计算机进行数值运算，就传数字给它，想让它处理文字，就传字符串给它

在Python3语言中一切皆是对象并且只有int没有long，

在Python3中如何判断变量指向什么数据类型:使用函数:type()

`

    str1 = 100
    str2 = '100'
    print(str1, type(str1))
    print(str2, type(str2))
`

在Python3中有六个标准的基本的数据类型，如下：
+ 整数类形(整形)：int
    - 在32位机器上，整数的位数为32位，取值范围为：-2**31 ~ 2**31，即-2147483648-2147483648
    - 在64位机器上，整数的位数为64位，取值范围为：-2**63 ~ 2**63，即-9223372036854775808-9223372036854775808

+ 字符串：str
    - 在Python中凡是用引号引起来的数据即字符串，不区别单引号或双引号
    
        `
        
            1、单双引号可以配合使用，例如
            content = 'I am yuxj, 18 year old'
            content = "I'm yuxj, 18 year old"
    
            2、三引号对字符串是可以换行的
            content = ''' 
                        每想你一次，
                        天上飘落一粒沙，
                        从此形成了撒哈拉。
                        每想你一次，
                        天上就掉下一滴水，
                        于是形成了太平洋。
                                   - 三毛
                      '''
        `
    - 字符串的拼接：+
        
        `
        
            1、str+str的拼接
            str1 = 'yu'
            str2 = 'xianjia'
            print(str1 + str2)
            
            2、str*int的拼接
            str3 = '坚强'
            print(str3 * 8)
        `

+ 布尔类型：boolean
    - 布尔类型只有两个值：True和False
    
        `
            
            print(2 > 1)    True
            print(3 < 1)    Fasle
            
        `
        

> ## 2.Python用户输入交互:input

+ 在Python3中，input() 函数接受一个标准输入数据，返回为 string 类型

+ 在Python2中， input() 相等于 eval(raw_input(prompt)) ，用来获取控制台的输入。

    `
    
        两者区别
        1、input() 和 raw_input() 这两个函数均能接收字符串，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
        而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个
        SyntaxError 。
        
        2、除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
        
        3、例子
            让用户输入姓名、年龄、性别，然后打印一句话'我叫： ，今年： ，性别：'
            name = input('请输入姓名：')
            age = input('请输入年龄：')
            sex = input('请输入性别：')
            msg = '我叫' + name + ', 今年' + age + ', 性别' + sex
            print(msg)
    `

