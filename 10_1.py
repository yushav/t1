#10_1
class Matrix:
    def __init__(self, lst_lst):
      self.lst_matrix = lst_lst

    def __str__(self):
      str_ = ''
      for i_ in range(len(self.lst_matrix)):
        str_ += ' '.join(map(str, self.lst_matrix[i_])) + '\n'
      return str_[:-1]

    def __add__(self, other):
      l1_ = len(self.lst_matrix)
      l2_ = len(other.lst_matrix)
      lst_ = []
      if l1_>=l2_:
        for i_ in range(l2_):
          lst_.append([x+y for x, y in zip(self.lst_matrix[i_], other.lst_matrix[i_])]
                     + (self.lst_matrix[i_])[l2_:])
        if l1_>l2_:
          lst_.append(*self.lst_matrix[l1_-l2_+1:])
      else:
        for i_ in range(l1_):
          lst_.append([x+y for x, y in zip(self.lst_matrix[i_], other.lst_matrix[i_])]
                     + (self.lst_matrix[i_])[l1_:])
        lst_.append(*self.lst_matrix[l2_-l1_+1:])
      
      return Matrix(lst_)      
      


mx2 = Matrix([[1,2],[3,4]])
print('матрица 1:')
print(str(mx2), '\n')

mx2_1 = Matrix([[2,1],[4,4]])
print('матрица 2:')
print(str(mx2_1), '\n')

mx3 = Matrix([[1,2,2],[3,4,3],[7,1,4]])
print('матрица 3:')
print(str(mx3), '\n')

print('матрица 1 + 2:')
print(str(mx2 + mx2_1))

print('матрица 3 + 1:')
print(str(mx3 + mx2))