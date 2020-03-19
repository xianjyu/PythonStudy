> python的while循环

生活中的循环：大气循环，歌曲列表循环等 

+ while的基本结构
 
    `while 条件： 循环体`

+ 初识循环

    ```
        while True:
            print("狼的诱惑")
            print("我们不一样")
            print("月亮之上)
            print("庐州月")
            print("人间")
            
        首先判断while循环的条件是否为True，如果是True进入循环体并执行到循环的底部后继续判断条件是否为True
        若条件一直成立，就会进入无限循环(死循环)
    ```
    
+ 循环如何终止
    
    - 改变判断条件
        ```
        
            flag = True     # 该方法时一种标志位
            while flag:
                print("狼的诱惑")
                print("我们不一样")
                print("月亮之上")
                print("庐州月")
                print("人间")
                flag = False
                
             上述代码只会执行一遍
      
      
            flag = True
            while flag:
                print("狼的诱惑")
                print("我们不一样")
                flag = False
                print("月亮之上")
                print("庐州月")
                print("人间")
            
            当条件在while循环体代码中时，初始条件满足时，进入循环体中，将条件改成不满足时
            此时程序执行玩循环体的代码便不再运行
      
        
        ```
    - break
       ```
           break：循环中遇到break时直接退出循环，后面的代码不会再运行
            while True:
                print("狼的诱惑")
                print("我们不一样")
                print("月亮之上")
                print("庐州月")
                print("人间")
                break
            
            while True:
                print("狼的诱惑")
                print("我们不一样")
                print("月亮之上")
                break
                print("庐州月")
                print("人间")
        
      ```
    
    - 系统命令
    
+ 继续循环：continue
    
    - 终止本次循环，继续下一次循环
    ```
        flag = True
        while flag:
            print('111')
            print('222')
            print('333')
            continue    # 不会再执行continue后面的代码，重新继续开始下一次循环
            print('444')

    ```



+ 练习题
    - 循环打印1-100的所有数字
        ```
            第一种
            count = 0
            flag = True
            while flag:  # 循环条件
                if count < 100:    # 判断count是否大于100
                    count = count + 1   # =为赋值
                    print(count)
                else:
                    flag = False    # 改变循环条件
      
      
            第二种
            count = 0
            while count < 100:
                count = count + 1
                print(count)
      
        ```
      
 - 练习题；1+2+3……+100的最终结果
 
    ```
        count = 0
        sum = 0
        while count <= 100:
            sum = sum + count
            count = count + 1
        print(count)
        print(sum)     
   
    ```
  
      
+ 练习题：1-100所有的偶数

    ```
        count = 1
        while count <= 100:
            if count % 2 == 0:
                print(count)
            count = count + 1
    ```


+ while else组合
    
    ```
        count = 1
        while count < 5:
            print(count)
            count = count + 1
        else:
            print(6)
    
      
        count = 1
        while count < 5:
            print(count)
            if count == 2:
                break
            count = count + 1
        else:
            print(6)
        while循环执行时被break打断，则不再执行else
  
    ```