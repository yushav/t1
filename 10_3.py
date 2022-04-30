#10_3
class Cell:
  def __init__(self, ct_cell):
    self.ct_cell = ct_cell
  
  def __add__(self, other):
    return Cell( self.ct_cell + other.ct_cell)

  def __sub__(self, other):
    dif_ = self.ct_cell - other.ct_cell
    if dif_ < 0:
      print('нельзя вычесть, результат < 0')
    else:
      return Cell( dif_)

  def __mul__(self, other):
    return Cell( self.ct_cell * other.ct_cell)

  def __floordiv__(self, other):
    return Cell( self.ct_cell // other.ct_cell)
    
  def __truediv__(self, other):
    return Cell( int(self.ct_cell / other.ct_cell))

  def make_order(self, ct_in_row):
    for i_ in range(self.ct_cell // ct_in_row):
      print('*'*ct_in_row)
    print('*'*(self.ct_cell % ct_in_row))


c1 = Cell(14)
c2 = Cell(20)

c1.make_order(5)
c2.make_order(5)
print('-'*10)

с3 = c1 + c2
с3.make_order(5)
print('-'*10)

c4 = c1 - c2
c4 = c2 - c1
c4.make_order(5)
print('-'*10)

(c1 / c4).make_order(5)
print('-'*10)

(c2 // c4).make_order(5)
print('-'*10)