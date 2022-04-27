#9_4
class Car:
    def __init__(self,speed, color, name, is_police):
      self.speed = speed
      self.color = color
      self.name = name
      self.is_police = is_police

    def show_speed(self):
      return self.speed
  
    def move__(self, speed):
      self.speed = speed
      return self.speed
        
    def go(self, speed):
      print(f'машина поехала, скорость {move__(self, speed)} км/ч')
        
    def stop(self):
      move__(self, 0)
      print(f'машина остановилась')
        
    def turn(self, direction):
      print(f'машина повернула, направление: {direction}')


class TownCar(Car):
    def __init__(self,speed, color, name, is_police):
      super().__init__(self,speed, color, name, 0)
  
    def show_speed(self):
      if self.speed > 60:
        print('Превышена разрешенная скорость движения 60 км/ч!')
      return self.speed

    
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
      super().__init__(self,speed, color, name, 0)

    
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
      super().__init__(self,speed, color, name, 0)

    def show_speed(self):
      if self.speed > 40:
        print('Превышена разрешенная скорость движения 40 км/ч!')
      return self.speed

    
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
      super().__init__(self,speed, color, name, 1)


car_police = PoliceCar(80, 'белый', 'Ford', 1)
car_work = WorkCar(60, 'оранжевый', 'Камаз', 0)
car_town = TownCar(79, 'желтый', 'volkswagen beetle', 0)
car_sport = SportCar(200, 'красный', 'Ferrari', 0)

car_work.show_speed()