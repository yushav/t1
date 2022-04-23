#5_2

n = input('input n: ')
odd_to_n = (num for num in range(1, int(n) + 1, 2))

#print(*odd_to_n)
for i_ in odd_to_n: #неявный вызов next()
  print(i_)