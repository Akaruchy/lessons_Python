# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

a = int(input())
b = int(input())
if a >= 0 & b >= 0:
    def sum(a, b):
        if b == 1:
            return (a+1)
        return sum(a+1, b-1)
    print(sum(a, b))
else:
    print("Ошибка! Введено отрицательное значение")
