# : На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input())
s = 0
for i in range(n):
    v = int(input()) # тут вводим значения, как они упали
    if v == 1:
        s += 1
print(s if s < n / 2 else n - s)


# Не поняла я условий задачи, даже пересматривая видео с семинара,
# не могу понять, зачем нам использовать циклы, когда нам нужно найти минимальное.
# Предположим, 5 монеток. они могли лечь как 5:0 так и 4:1. Если учитывать что точно
# есть и решка и орел, тогда минимальное 1. Нас же не просят указать дополнительно сколько
# орлов, а сколько решек?  При всех возможных комбинациях ( 5:0, 4:1, 3:2, 2:3, 1:4, 0:5)
# максимальное количество действий для переворота это 2.
# Так что же от меня требует задача? Помогите!#

# n = int(input())
# min = n // 2
# print(min)