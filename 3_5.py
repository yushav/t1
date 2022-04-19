#3_5
from random import sample, choices

def get_jokes( n, repl='n'):
  """
  :repl: allows you to get unique or duplicate selections
  :return: zipType
  """
  nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
  adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
  adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

  if repl == 'n':
    l1_ = sample( nouns, n)
    l2_ = sample( adverbs, n)
    l3_ = sample( adjectives, n)
  else:
    l1_ = choices( nouns, k=n)
    l2_ = choices( adverbs, k=n)
    l3_ = choices( adjectives, k=n)

  return zip( l1_, l2_, l3_)


n_ = int(input("сколько шуток? "))
print( *get_jokes( n_))
print( *get_jokes( n_, repl='y'))
print( help(get_jokes))