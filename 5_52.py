#5_5_2

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

lst_unique = [i for i in src if i not in (src[src.index(i)+1:])]

print(lst_unique)