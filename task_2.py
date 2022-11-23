# 2) Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds_initial = int(input("Введите количество секунд: "))

seconds = seconds_initial % 60
minutes_all = seconds_initial // 60
minutes = minutes_all % 60
hours = minutes_all // 60

print("{}:{}:{}".format(hours, minutes, seconds))
