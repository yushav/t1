#1_2

numb_lst = [1]
sum_numb = 0
sum_numb17 = 0
for i in range(3, 1000, 2):
  _n = i ** 3
  numb_lst.append(_n)
  _n_str = str(_n)
  _n_str17=str(_n+17)
  _sum=0
  _sum17=0
  for j in _n_str:
    _sum += int(j)
  if not _sum % 7:
    sum_numb +=_n
  for j17 in _n_str17:
    _sum17 +=int(j17)
  if not _sum17 % 7:
    sum_numb17 +=_n + 17
  
#print( *numb_lst)
print(sum_numb, sum_numb17)