# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = 0
y = 0
z = 0
count = 0
while count < 8:
    count_bin = format(count, 'b')
    if len(count_bin) == 1:
        z = count_bin[0]
    elif len(count_bin) == 2:
        y = count_bin[0]
        z = count_bin[1]
    else:
        x = count_bin[0]
        y = count_bin[1]
        z = count_bin[2]
    print(f"not ({x} or {y} or {z}) == (not {x} and not {y} and not {z})")
    if not (x or y or z) == (not x and not y and not z):
        print("true")
    else:
        print("false")
    count = count + 1
