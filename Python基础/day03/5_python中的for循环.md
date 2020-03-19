> ## for循环

+ len：获取可迭代对象的元素的总个数
    
     print(len(msg))
    
+ 基本结构
    
    for 变量 in iterable(可迭代对象)    

+ 语法
    
    - break
    
            s = 'yuxj'
            for i in s:
                if i == 'x':
                    break
                print(i)   # y u
                 
            s = 'yuxj'
            for i in s:
                print(i)   # y u x
                if i == 'x':
                    break
                 
    - continue
    
            s = 'yuxj'
            for i in s:
                if i == 'x':
                    continue
                print(i)   # y u x j
    
    - for else和while else用法一样
            
            msg = 'yuxj'
            for i in msg:
                if i == 'x':
                    break
                print(i)
            else:
                print('……')     # for循环执行时被break打断，else则不会再执行
            
            
            msg = 'yuxj'
            for i in msg:
                print(i)
            else:
                print('……')     # for循环执行时被break打断，else则不会再执行












+ while循环打印出：yuxj中的每一个字符
        
     - while循环
             
            s = 'yuxj'
            index = 0
            while index < 4:
                print(s[index])         # y u x j
                index += 1
        
     - for循环
            
            s = 'yuxj'
            for i in s:
                print(i)     # y u x j
                