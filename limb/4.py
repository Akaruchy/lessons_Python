# Условие
# Дано натуральное число. Требуется определить, является ли год с 
# данным номером високосным. Если год является високосным, то выведите YES, 
# иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также 
# если он кратен 400.
print("введите год:")
n = int(input())
if n % 4 == 0 and n % 400 :
    if n % 100 == 0:
        print ("високосный")
    print ("високосный")   
else:
    print ("невисокосный")