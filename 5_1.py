#5_1

def odd_nums(max_num):
  for num in range(1, int(max_num) + 1, 2):
    yield num


n = input('input n: ')
odd_to_n = odd_nums(n)
#print(*odd_to_n)
for i_ in odd_to_n: #неявный вызов next()
  print(i_)