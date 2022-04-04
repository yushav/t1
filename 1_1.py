sec_lst = [53, 153, 4153, 400153]
for sec in sec_lst:
  s_out = ''
  print('duration = ', sec)
  
  days = sec // (60 * 60 * 24)
  if days:
    s_out += str(days) + ' дн '
  _mod = sec % (60 * 60 * 24)
  
  hours = _mod // (60 * 60)
  if hours:
    s_out += str(hours) + ' час '
  _mod = _mod % (60 * 60)
  
  mins = _mod // 60
  if mins:
    s_out += str(mins) + ' мин '
  _mod = _mod % 60
  
  if _mod:
    s_out += str(_mod) + ' сек'
  print(s_out)
