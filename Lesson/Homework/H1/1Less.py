# Найдите сумму чисел трехзначного числа

n = int(input())
u = 0

while n > 0:
    x = n % 10
    n = n // 10
    u = u + x
    print(n)
print(u)