""" 
元组/二维元组 小括号
a = (0,1,2,3,4)
b = (a,5,6,7,8)
print(b[0][3]) #b[0] ->a ,查找b数组中a内的3下标
print(b[1:3]) # 切片：查找b数组中下标1-3的内容，左闭右开，：前后不写表示开头结尾

 """


# 数组 中括号
from pickle import APPEND
from tkinter import INSERT


""" a = [1,2,3,4,5,6] 
a.append('append') #往数组末尾追加数据
a.insert(1,'insert') #往数组指定位置追加数据
b = a.pop(0) # 剪切指定下标数据，赋值给b（pop剪切数据存储）,取值第一次下标为0的数据
c = a.pop(1) # 上面已经剪切过一次数组，这里剪切取值第二次数据
print(a)
print(b+c) """

