# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt
# в одной строке одно число.

key = ['0\n', '1\n', '2\n'] #Создаем файл с ключами
data = open('file.txt', 'w')
data.writelines(key)
data.close()

num = int(input('Введите число = '))
arr = []
for i in range(-abs(num), abs(num) + 1, 1): #создаем диапазон и записываем в список
    arr.append(i)
print(arr)

path = 'file.txt' # считываем ключи с файла
data = open(path, 'r')
dlist = [int(line.strip()) for line in data]
print(dlist)
data.close()

mult = 1 #Перемнажаем числа по записанным ключикам.
for i in dlist:
    mult = mult * arr[i]
print(mult)
exit()

