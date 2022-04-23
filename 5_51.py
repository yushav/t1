#5_5_1

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

lst_unique = []
lst_unique.append(src[0])

for i_ in src[1:]:
  if i_ in lst_unique:
    lst_unique.remove(i_)
  else:
    lst_unique.append(i_)

print(lst_unique)