for numb in range(1, 21):
  s_out = str(numb)
  if numb == 1:
    s_out += ' процент'
  elif numb > 1 and numb < 5:
    s_out += ' процента'
  else:
    s_out += ' процентов'
  print( s_out)