""" name = str(input("请输入您的名字："))
age = int(input("请输入您的年龄："))
sex = str(input("请输入您的性别：")) """

a = {"姓名":str(input("请输入您的名字：")),"age":int(input("请输入您的年龄：")),"sex":str(input("请输入您的性别："))}
# 输入赋值并以键值对结构存入字典

print("您的姓名：",a["姓名"])
print("您的年龄：",a["age"])
print("您的性别：",a["sex"])

a.update(姓名="超")
# 更新字典里key为姓名的值
print("更新字典姓名第二次输出",a)

del a["姓名"]
# 删除字典里key为姓名的值
print("删除字典姓名第三次输出",a)