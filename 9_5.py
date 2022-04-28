#9_5
class Stationery:
    def __init__(self, title):
      self.title = title

    def draw(self):
      print(f'{self.title} запуск отрисовки')


class  Pen(Stationery):
    def __init__(self, title):
      super().__init__(title)
  
    def draw(self):
      print(f'{self.title} запуск отрисовки - линия')

    
class  Pencil(Stationery):
    def __init__(self, title):
      super().__init__(title)
  
    def draw(self):
      print(f'{self.title} запуск отрисовки - штриховка')

    
class  Handle(Stationery):
    def __init__(self, title):
      super().__init__(title)
  
    def draw(self):
      print(f'{self.title} запуск отрисовки - надпись')


black_pencil = Stationery('черный карандаш')
blue_pen = Pen('синяя ручка')
green_pencil = Pencil('зеленый карандаш')
red_handle = Handle('красный маркер')

black_pencil.draw()
blue_pen.draw()
green_pencil.draw()
red_handle.draw()