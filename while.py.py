while True:
    number = int(input('Введите число: '))
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    if number % 1 == 0:
        print("Положительное число ")
        continue
    elif number % -0 == 0:
        print("Отрицательное число")
    else:
        break
print('Выход за границу')