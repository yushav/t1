#2_2

def is_int (value):
  try:
    int(value)
  except ValueError:
    res = False
  else:
    res = True
  return res

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst1 = []

for item in lst:
  i_=[]
  if is_int(item):
    if len(item) == len(str(int(item))):
        i_ = ['"', f'{int(item):02}', '"']
    else:
      i_ = ['"', f'{item[0]}{int(item):02}', '"']
  else:
    i_ = [item]
  lst1.extend(i_)
 
print( *lst1) 
print( lst1) 