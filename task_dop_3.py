# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input("Введите X не равный 0: "))
y = int(input("Введите Y не равный 0: "))
if x > 0 and y > 0:
    print(f"Точка ({x}|{y}) находится в первой четверти")
elif x < 0 and y > 0:
    print(f"Точка ({x}|{y}) находится в второй четверти")
elif x < 0 and y < 0:
    print(f"Точка ({x}|{y}) находится в третьей четверти")
elif x > 0 and y < 0:
    print(f"Точка ({x}|{y}) находится в четвертой четверти")

# Условие "X ≠ 0 и Y ≠ 0"
# делает бессмысленным задание "(или на какой оси она находится)"