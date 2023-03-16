# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

n = input('Введите общее количество монеток на столе: ')

while not n.isdigit():
  n = input('Вы ввели не натуральное число, попробуйте еще разок: ')

n = int(n)
coins=[]

for i in range(n):
  coins.append(random.randint(1, 2))
  
print (coins)

coat = 0
tails = 0

for i in range(n):
  if coins[i] == 1:
    coat += 1
  else:
    tails += 1

if tails > coat:
  print (f'Минимальное количество монет, которые надо перевернуть равно {coat}')
else:
  print(f'Минимальное количество монет, которые надо перевернуть равно {tails}')