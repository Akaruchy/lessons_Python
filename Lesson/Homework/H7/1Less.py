# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе
# несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# gl = ["а", "e", "ё", "о", "и", "ы", "э", "ю", "у", "я",]
# stroka1 = str(input("первая строка", ))
# stroka2 = str(input("Вторая строка", ))

# m1 = [i for i in stroka1]
# print(m1)
# count1 = 0
# for i in m1:
#     if i in gl:
#         count1=count1+1

# m2 = [i for i in stroka2]
# print(m2)
# count2 = 0
# for i in m2:
#     if i in gl:
#         count2=count2+1

# if count1 == count2:
#     print("Парам пам-пам")
# else:
#     print ("Пам парам")

stroka1 = str(input())
gl = ["а", "e", "ё", "о", "и", "ы", "э", "ю", "у", "я",]
st = stroka1.split()
print(st)
list = []
for i in st:
    count = 0
    for b in i:
        if b in gl:
            count = count+1
            print(count)
    list.append(count)

print (list)
if len(set(list)) == 1:
    print("Парам пам-пам")
else:
    print ("Пам парам")