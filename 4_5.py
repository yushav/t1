#4_5
import utils

if __name__ == '__main__':
  import sys
  print( *map( utils.currency_rates, sys.argv[1:]))