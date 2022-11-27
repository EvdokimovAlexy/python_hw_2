# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число\nnum = '))

factorial = 1
arr = []
for i in range(1, n+1):
    factorial = factorial * i
    arr.append(factorial)
print(arr)