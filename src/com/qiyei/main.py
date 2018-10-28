
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
