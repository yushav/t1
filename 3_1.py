#3_1

def num_translate( eng):
  dict_num = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
  }
  try:
    rus = dict_num[eng]
  except KeyError:
    rus = 'None'
  return(rus)

eng = input("введите число 1-10 по-английски: ")
print('по-русски: ',num_translate( eng))