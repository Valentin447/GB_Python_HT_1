# 1) Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 10
b = 12.5
c = "test"
print(a, b, c)

users_number_1 = int(input("Введите целое число: "))
users_number_2 = float(input("Введите дробное число: "))
users_str_1 = input("Введите первую строку: ")
users_str_2 = input("Введите вторую строку: ")
print(f"Целое число 1 = {users_number_1}, дробное число = {users_number_2}, "
      f"строка 1 = {users_str_1}, строка 2 = {users_str_2}")
