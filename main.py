def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите любое вещественное число: ')
print(f'Сумма цифр в этом числе равна {sum_digits(num)}')

# Если на вход попадает значение типа float, то достаточно перевести значение в тип str (str(num).replace...)