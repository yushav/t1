#3_3

def thesaurus( *args):
  dict_name = {}
  for i_ in args:
    dict_name.setdefault(i_[0], list( filter( lambda x: x.startswith(i_[0]), args)))
  return(dict_name)


lst_name = ["Юрий", "Василий", "Иван", "Мария", "Петр", "Виктор", "Илья"]
dict_name = thesaurus(*lst_name)
print(dict_name)

list_keys = list(dict_name.keys())
list_keys.sort()
for i_ in list_keys:
  print(i_,dict_name[i_])