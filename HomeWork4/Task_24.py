# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

strN = input('Введите общее количество кустов на грядке: ')

while not strN.isdigit() or int(strN) < 1:
  strN = input('Вы ввели не натуральное число, попробуйте еще разок: ')
N = int(strN)

berries = list()

for i in range (N):
  temp = input(f'Введите количество ягод на кусте {i+1}: ')
  while not temp.isdigit() or int(temp) < 1:
    temp = input('Вы ввели неправильное количество, давайте заново: ')
  berries.append(int(temp))

collect = list()
for i in range(1,N-1):
  collect.append(berries[i-1] + berries[i] + berries[i+1])

print(f'Максимальное число ягод за один проход: {max(collect)}')