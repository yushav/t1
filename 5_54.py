#5_5_4
import random
from time import perf_counter

#src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src = [random.randrange(1,1000) for i in range(10000)]

start = perf_counter()
set_unique = set()
tmp = set()

for i_ in src:
  if i_ not in tmp:
    set_unique.add(i_)
  else:
    set_unique.discard(i_)
  tmp.add(i_)

lst_unique = [i for i in src if i in set_unique]
end = perf_counter()
print(lst_unique, end - start)
#5_53 35.56636882800376
#5_52 7.430894619996252
#5_51 1.4
#5_54 0.06