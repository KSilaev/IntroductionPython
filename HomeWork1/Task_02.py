# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = input('Введите трехзначное число: ')

while not num.isdigit() or len(num) != 3:
  num = input('Вы ввели не трехзначное число, попробуйте еще разок: ')

sum = 0
for i in range(len(num)):
  sum += int(num[i])

print (sum)
