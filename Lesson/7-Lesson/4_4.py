# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).

def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1


values = [0, 2, 10, 5]
print(same_by(lambda x: x % 2, values))

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')