a = 10 
# 根据该数判断类型
if a == "":
    print("请输入内容")
    exit()
if type(a) is int:
    print("整数")
elif type(a) is float:
    print("小数")
elif type(a) is str:
    print("字符串")
else:
    print("请输入正确内容")

