#9_1
import time


class TrafficLight:
    def __init__(self):
        self.__color = 'red'
        self.__color_duration = {
          'red' : 7,
          'yellow' : 2,
          'green': 10,
        }

  
    def running(self, color):
      _r = self.__color == 'red' and color == 'yellow'
      _y = self.__color == 'yellow' and color == 'green'
      _g = self.__color == 'green' and color == 'red'
      if _r or _y or _g:
        self.__color = color
        print( color)
        time.sleep(self.__color_duration[color])
        res = 1
      else:
        res = 0
    
      return res


tl = TrafficLight()
print('red')

#tl.running('yellow')
#tl.running('green')
#tl.running('red')

while tl.running( input('цвет?: ')):
  pass
print('ошибка')