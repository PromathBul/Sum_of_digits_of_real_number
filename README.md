# Задача
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Решение
С помощью функции `replace` удаляем из строки точку и минус.

Далее, используя `map` кадый элемент строки конвертируем в тип `int` и получаем сумму элементов.