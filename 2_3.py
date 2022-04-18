#2_3

def is_int (value):
  try:
    int(value)
  except ValueError:
    res = False
  else:
    res = True
  return res

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i_ = 0
n_ = len(lst)

while i_ < n_:
  if is_int(lst[i_]):
    lst.insert(i_, '"')
    if len(lst[i_+1]) == len(str(int(lst[i_+1]))):
      lst[i_+1] = f'{int(lst[i_+1]):02}'
    else:
      lst[i_+1] = f'{lst[i_+1][0]}{int(lst[i_+1]):02}'
    lst.insert(i_+2, '"')
    i_ += 3
    n_ += 2
  else:
    i_ += 1
 
print( *lst)   
print( lst)