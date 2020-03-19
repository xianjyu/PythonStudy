> ## 字符串的常用操作方法

+ upper：大写，不会对原字符串进行任何操作，都是产生一个新的字符串

        s = 'Yuxj'
        print(s.upper())

+ lower：小写，不会对原字符串进行任何操作，都是产生一个新的字符串

        s = 'Yuxj'
        print(s.lower())
        
        
        应用
            输入验证码，不区分大小写
            username = input('请输入用户名：')
            password = input('请输入密码：')
            code = 'QweR'
            you_code = input('请输入验证码：')
            if you_code.upper == code.upper:
                if username == 'yuxj' and password == 'yuxj':
                    print('登录成功')
                else:
                    print('用户名或密码错误')
            else:
                print('验证码错误')


+ startswith：以什么开始
        
        - 返回的是bool类型
        s = 'yuxj'
        print(s.startswith('y'))    # True
        
        print(s.startswith('u',1 ,3))   # True    

+ endswith：以什么结束
        
        s = 'yuxj'
        print(s.endswith('u', -4, -3))
        

+ replace：替换

            s = 'yuxj很nb，yuxj是男性，yuxj长得很帅'
            print(s.replace('yuxj', 'YUXJ'))    # 全部替换
            print(s.replace('yuxj', 'YUXJ', 1))     # 替换第一个
            print(s.replace('yuxj', 'YUXJ', 2))     # 替换第二个
            print(s.replace('yuxj', 'YUXJ', 1, 3))  # TypeError: replace expected at most 3 arguments, got 4
        
             
+ strip：去掉空格                
        
     - 去掉前后空格   
     
            s = '  \n学习\t '
            print(s.strip())
            print(s.rstrip())
            print(s.lstrip())
            
     - 去掉指定的空格
           
            s = '你abcdef好'
            s2 = s.strip('你好')  # 取出指定的字符：abcdef，只要头尾包含有指定字符序列中的字符就删除
            print(s2)
        
        
+ split：切割，字符串转化列表
    
    - 默认按照空格分隔
        
            s = 'a b c'
            print(s.split())    # ['a', 'b', 'c']    
            
    - 切割后的个数等于分隔符+1
            
            s = 'a:b:c'
            print(s.split(':'))
            # [a', 'b', 'c']  
            
            s = ':a:b:c'
            print(s.split(':'))     # ['', a', 'b', 'c']    
            print(s.split(':', 2))      # ['', 'a', 'b:c']，只切割前两个
        
        
+ join：连接，列表转化成字符串

    - 前提：列表中的元素必须都是字符串类型
    
            s = ['a', 'b', 'c']
            print(':'.join(s))     # a:b:c
            
    - 否则，报类型错误
        
            s = ['a', 'b', 1]
            print(':'.join(s))  # TypeError: sequence item 2: expected str instance, int found

+ count：计算某个字符串中的字符串出现的次数
        

+ format格式化输出

    - 第一种
        
            msg = '我叫{}，今年{}，性别{}'.format('yuxj', 25, '男')
            print(msg)
    
    - 第二种
                 
            msg = '我叫{0}，今年{1}，性别{2}，我依然叫{0}'.format('yuxj', 25, '男')
            print(msg)    
                     
    - 第三种
    
            msg = '我叫{name}，今年{age}，性别{sex}'.format(age=25, name='yuxj', sex='男')
            print(msg)
            
            
+ is系列

    - 字符串是否由字母或数字组成
        
            msg = '123abc456' 
            print(msg.isalnum())     # True
            
    - 字符串是否由字母组成
            
            msg = 'abc'
            print(msg.isalnum())    # True
    
    - 字符串是否由数字组成
    
            msg = '123456'
            print(msg.isalnum())     # True
            
    - 字符串是否由十进制组成         
        
            msg = input('请输入数字：')
            if msg.isdecimal():
                print(int(msg))
            else:
                print('输入有误')
        
               
+ in 和 not in 
    
     - in
        
            msg = 'yuxj'
            print('y' in msg)   # True
            
     - not in           
            
            msg = 'yuxj'
            print('y' not in msg)   # False