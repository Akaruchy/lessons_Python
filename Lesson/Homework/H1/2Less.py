# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
# сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# журавликов, чем Петя и Сережа вместе?
# 2Less

sum = int(input("всего журавликов:"))
print(sum)
x = int(sum / 6)
# y = int(2 * (x + x))
y = int(4*x)
# y = int(2*x + 2*x)

# x = int(x // -1)
# x = x * -1
# y = int(y)

if y % 2 == 0:
    x = x + 1
# else:
#     y = y + 1

print("Катя сделала:")
print(y)
print("Сережа и Петя сделали по")
print(x)
