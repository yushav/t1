#8_4
from functools import wraps

def val_checker(f):
  def _val_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for key in args:
        if f(key):
          print(f'{func.__name__}( {key}: {type(key)})')
        else:
          raise ValueError ( f'wrong val: {key}' )
      res = func(*args,**kwargs)
      return res
  
    return wrapper
  return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


a = calc_cube(5)
a = calc_cube(-5)
