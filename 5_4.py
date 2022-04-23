#5_4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def iter(lst):
  for i in range(len(lst)-1):
    yield (lst[i], lst[i+1])
 

print( [j_ for i_, j_ in iter(src) if i_ < j_])