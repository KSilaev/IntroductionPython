# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = input('Введите число N: ')

while not N.isdigit() or int(N) < 1:
  N = input('Вы ввели неправильное число, попробуйте еще разок: ')

N = int(N)
i = 0
print(f'Степени двойки меньше {N}:')
while 2 ** i <= N:
  print(2**i)
  i+=1