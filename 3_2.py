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
  return(dict_num.get(eng))


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
  rus = dict_num.get(eng)
  if rus is None:
    rus = dict_num.get(eng[0].lower()+eng[1:])
    if rus is not None:
      rus =rus.capitalize()
  return(rus)


eng = input("введите число 1-10 по-английски: ")
print('по-русски: ',num_translate( eng))
print('по-русски: ',num_translate_adv( eng))
