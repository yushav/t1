#2_5

lst_prices = [57.8, 46.51, 97, 105.03, 1.07, 110.10, 0.03, 1000, 55.11, 1]


def rub_cent (lst):
  lst_out = []

  for i in lst:
    cent = i % 1
    rub = int(i - cent)
    lst_out.append(f'{rub}руб {int(round(cent,2)*100):02}коп')
  
  return lst_out

print(','.join(rub_cent(lst_prices)))
print(id(lst_prices))

lst_prices.sort()
print(','.join(rub_cent(lst_prices)))
print(id(lst_prices))

lst_sort = sorted( lst_prices, reverse=True)
print(','.join(rub_cent(lst_sort)))
print(id(lst_sort))

print('цены 5и самых дорогих товаров: ', ','.join(rub_cent(lst_sort[:5])))