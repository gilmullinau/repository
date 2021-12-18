
import math
from datetime import datetime

f = open('file.txt')
numbers_file = f.read()
f.close()

numbers = numbers_file.split()

N = len(numbers)

# Тест: только цифры без букв
okey = False
for i in range(N):
    number = numbers[i]
    if number.isdigit() == False:
        print("Ошибка: это не число:", number)
    else:
        okey = True

if okey == True:
    # определяем время старта
    time1 = datetime.today()
    for i in range(N):
        numbers[i] = int(numbers[i])
    n_max = max(numbers)
    n_min = min(numbers)
    summa = sum(numbers)
    prod = 1
    for i in range(N):
        prod = prod * numbers[i]
        if prod > 99999999:
            print("Ошибка: очень большое произведение")
            prod = 0
            break
    print("Минимум ", n_min)
    print("Максимум ", n_max)
    print("Сумма ", summa)
    print("Произведение ", prod)
    # определяем время окончания
    time2 = datetime.today()
    time_x = time2 - time1
    time_sec = time_x.seconds
    print("Время работы ", time_sec, "секунд",  "Количество чисел ", N)


if okey == True:
    s = 0
    p = 1
    for i in range(N):
        number = numbers[i]
        if number > n_max:
            print("Ошибка: макимум неправильный")
        if number < n_min:
            print("Ошибка: минимум неправильный")
        s = s + number
        p = p * number
    if s != summa:
        print("Ошибка: сумма неправильная")
    if p != prod:
        print("Ошибка: произведение неправильное")

