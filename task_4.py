# 4) Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_value = 0
current_number = number
while current_number > 0:
    current_value = current_number % 10
    if current_value > max_value:
        max_value = current_value
    current_number = current_number // 10
print(f"Самая большая цифра числа {number} это {max_value}")
