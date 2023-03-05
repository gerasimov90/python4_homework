#Задача 22
mol = [int(x) for x in input('Введите через пробел количество элементов в двух множествах: ').split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
a = [int(x) for x in input('Введите через пробел элементы первого множества: ').split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [int(x) for x in input('Введите через пробел элементы второго множества: ').split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')