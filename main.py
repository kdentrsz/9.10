n = int(input('Сколько людей вы хотите взвесить? '))
k = 0
sum = 0
for i in range(n):
  m = int(input())
  k += 1
  sum += m
  sr = sum/k
if sum > 350:
  print("Вы не можете ехать вместе в лифте")
print("Средний вес людей = ",sr)
print("Общий вес = ",sum)
