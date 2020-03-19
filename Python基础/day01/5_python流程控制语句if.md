> ## Python流程控制语句if
生活中经常遇到的各种选择和判断在程序中也会遇到，比如玩色子，猜大小，比如选择哪条路回家？Python程序中同样也会遇到。IF语句就是用作条件判断的控制语句

+ 语法一：

    ``` 
    
        单独if
            if 条件:　　# 引号是将条件与结果分开
    　　         结果1  # tab键，告诉程序满足这个条件
            结果2　　# 如果条件是真（True）执行结果1，然后结果2，如果条件假False，直接结果2.
    
    ``` 

+ 语法二：

        ```          
            if与else
            
            if条件：
    
            　　结果1
            else：
            　　结果2
            
            代码3
        ```


+ 语法三：

   ``` 
        
            if、elif、elif
            if条件：
            　　结果1
            elif：
            　　结果2
            elif:
                结果3
    ``` 

+ 语法四：

    ``` 
        
        if、elif、elif、else
        if条件：
        　　结果1
        elif：
        　　结果2
        elif:
            结果3
        else:
            结果4
    ``` 

    
+ 语法五：if嵌套

    ``` 
            if 条件1:
            　　结果1
            　　if条件2：
            　　　　结果2
            　　　　else：
            　　　　　　结果3
            else：
            　　结果4  ###  可以无限嵌套，但是在实际开发中，不要超过三层嵌套。
  
            username = input('请输入用户名：')
            password = input('请输入密码：')
            you_code = input('请输入验证码：')
            
            code = 'qwer'
            
            if you_code == code:
                if username == 'yuxj' and password == 'yuxj':
                    print('登录成功')
            else:
                print('验证码错误')
    ``` 
  
  
  
  
  


  