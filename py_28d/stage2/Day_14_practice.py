# 1. 定义 Student 类
class Student:
    # 初始化方法，接收姓名和年龄作为参数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义一个简单的方法
    def study(self):
        print(f"{self.name} 正在努力学习。")

# 2. 创建 3 个实例
student1 = Student("张三", 20)
student2 = Student("李四", 21)
student3 = Student("王五", 19)

# 3. 验证结果（可选：调用属性和方法）
print(student1.name, student1.age)
student1.study()