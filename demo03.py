name = str(input("请输入您的名字："))
age = int(input("请输入您的年龄："))
sex = str(input("请输入您的性别："))

a = {"name":name,"age":age,"sex":sex}
# 输入赋值并以键值对结构存入字典

a.update(name="超")
# 更新字典里key为name的值

print("您的姓名：",a["name"])
print("您的年龄：",a["age"])
print("您的性别：",a["sex"])