# Задайте словарь из n чисел последовательности (1 + (1/n))^n и
# выведите на экран их сумму.
# Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
# Необходимо сложить все значения словаря и вывести  сумму на экран.

n = int(input('Введите число\nnum = '))
n_list = {}
for i in range(1, n+1):
   n_list[i] = (1 + (1 / i)) ** i
print(n_list)