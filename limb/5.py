# Условие
# Даны три целых числа. Выведите значение наименьшего из них.

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
elif c > b and c > a:
    max = c
print (max)
