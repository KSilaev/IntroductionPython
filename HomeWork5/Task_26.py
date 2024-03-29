# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree(A, B):
  if B == 0:
    return 1
  return A * degree(A, B - 1)

strA = input('Введите число, которое будем возводить в степень: ')

while not strA.isdigit():
  strA = input('Вы ввели не натуральное число, попробуйте еще разок: ')
A = int(strA)

strB = input('Введите степень, в которую будем возводить: ')

while not strB.isdigit():
  strB = input('Вы ввели не натуральное число, попробуйте еще разок: ')
B = int(strB)

print(f'Число {A} в степени {B} равно {degree(A, B)}')