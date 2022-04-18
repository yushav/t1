#3_2

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

def num_translate_adv( eng):
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
    try:
      rus = dict_num[eng[0].lower()+eng[1:]].capitalize()
    except KeyError:
      rus = 'None'
  return(rus)

eng = input("введите число 1-10 по-английски: ")
print('по-русски: ',num_translate( eng))
print('по-русски: ',num_translate_adv( eng))
