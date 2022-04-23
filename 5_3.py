#5_3

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Денис'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def zip_lists( list1, list2):
  len_l1 = len(list1)
  len_l2 = len(list2)

  yield zip(list1, list2 +
              [None for i_ in range(len_l1 - len_l2)
               if len_l2 < len_l1])

    
#tutors_klasses = (t_k for t_k in zip(tutors, klasses))

tutors_klasses = zip_lists( tutors, klasses)
print( type(tutors_klasses))
for i_ in tutors_klasses:
  print( *i_)