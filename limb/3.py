# Условие
# Заданы две клетки шахматной доски. Если они покрашены в один цвет,
#  то выведите слово YES, а если в разные цвета — то NO. Программа 
# получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца 
# и номер строки сначала для первой клетки, потом для второй клетки.
print ("введите координаты 1 клетки:")
xn = int(input("x:"))
yn = int(input("y:"))
print ("введите координаты 2 клетки:")
xm = int(input("x:"))
ym = int(input("y:"))

if xn % 2 == 0:
    xn = str("чет")
else:
    xn = str("нечет")
if xm % 2 == 0:
    xm = str("чет")
else:
    xm = str("нечет")
if yn % 2 == 0:
    yn = str("чет")
else:
    yn = str("нечет")
if ym % 2 == 0:
    ym = str("чет")
else:
    ym = str("нечет")    
print (xn, yn, xm, ym)

if xn == str("чет") and yn == str("чет") or xn == str ("нечет") and yn == str ("нечет"):
    a = str("черн")
else:
    a = str("бел")

print (a)

if (xm == str("чет") and ym == str("чет")) or (xm == str ("нечет") and ym == str ("нечет")):
    b = str("черн")
else:
    b = str("бел")

print (b)

if a == b:
    print("yes")
else:
    print("no")


