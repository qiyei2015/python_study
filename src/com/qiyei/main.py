"""主函数"""

from com.qiyei.animal import Dog
from com.qiyei.car import Car, ElectricCar

print("hello world")

even_numbers = list(range(2, 25, 2))
print(even_numbers)

# 循环
for num in even_numbers:
    print(num ** 2)

print(max(even_numbers))
print(min(even_numbers))
print(sum(even_numbers))

# 列表解析
squares = [item ** 2 for item in range(1, 25)]
print(squares)

my_dog = Dog("张三", 58)
print("age:" + my_dog.name + " age:" + str(my_dog.age))
my_dog.sit()
my_dog.roll_over()

my_electric_car = ElectricCar("宝马", "X6", 20181029)

print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()
