# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input())
list = [i for i in range(1, n + 1)]
print(list)
x = int(input())
if x > max(list):
    print("-> ", max(list))
else: 
    print(x) # выводим введенное число, так как если Х в списке, самое близкое к нем - оно же само. Или я не поняла условия задачи.
