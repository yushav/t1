#8_3
def type_logger(func):
  def wrapper(*args):
    for key in args:
      print(f'{func.__name__}( {key}: {type(key)})')
    
    res = func(*args)
    return res

  return wrapper

@type_logger
def calc_cube(x):
   return x ** 3


a =calc_cube(5)
