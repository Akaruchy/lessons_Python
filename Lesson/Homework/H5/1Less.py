# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

num_a = int(input())
num_b = int(input())
def step(num_a, num_b):
    if (num_b == 1):
        return num_a
    if (num_b != 1):
        return num_a * step(num_a, num_b - 1)
print(step(num_a, num_b))
