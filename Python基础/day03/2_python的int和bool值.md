+ int 
    - 主要用于计算 + - * /
    + 二进制转化成十进制
        - 0001 1010  ----> 26 
        - b = 0 * 2**0 + 1 * 2**1 + 0 * 2**2 + 1 * 2**3 + 1 * 2**4
    + 十进制转化成二进制
        - 42转化成二进制
              2  42         …… 0    被整除为0
              2  21         …… 1    没有被整除为1
              2  10         …… 0     
              2  5          …… 1
              2  2          …… 0
                 1          …… 1    从下往上算
                 
        - 十进制为101010    > 0010 1010
        
    + bit_length 有效的二进制长度
        
        ```
            i = 4
            print(i.bit_length())   # 3
            
            i = 42
            print(i.bit_length())   # 6
            + str
        ```
       

+ bool
    
    + int ---> bool
        - True - 1
        - False - 0
        - 非零即True，零即False
        
    + str ---> bool
        - s = ' ',   print(boo(s))      # 空格,True
        - s = '',    print(bool(s))     # 空字符串,False
        
        ```
            
            s = input('请输入内容')
            if s:
                print('有内容')    # 输入空格
            else:
                print('没有输入任何内容')      
        ```
      
      
      
      