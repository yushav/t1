#8_3
from functools import wraps

def type_logger(func):
  @wraps(func)
  def wrapper(*args):
    for key in args:
      print(f'{func.__name__}( {key}: {type(key)})')
    res = func(*args)
    return res

  return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

@type_logger
def calc_xy(x, y):
   return x ** y

a =calc_cube(5)
b =calc_xy(5, 2)
