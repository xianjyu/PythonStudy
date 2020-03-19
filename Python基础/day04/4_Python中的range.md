> ## range

+ range
    
    - 类似于列表，自定制数字范围的数字列表
    
            for i in range(10):
                print(i)    # 0-9，顾头不顾腚
            
            for i in range(2, 11, 2):
                print(i)
            
            for i in range(10, 0 , -2):
                print(i)
     
    - range多半与for循环结合使用
            
            利用for循环和range将l列表的所有索引依次打印出来
            l = [1, 2, 3, 'alex', 'yuxj']   
            count = 0
            for i in l:
                print(count)
                count += 1
            
            for i in range(len(l)):
                print(i)     
                
    - for循环中的代码为pass，循环依然执行
        
            for i in range(3):
                pass
            print(i)    # 2