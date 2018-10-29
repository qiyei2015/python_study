"""动物定义"""

# 定义类
class Dog():
    """这是一只狗"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sit")

    def roll_over(self):
        print(self.name.title() + " is roll_cover")

