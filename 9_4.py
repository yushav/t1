#9_4
class Car:
    def __init__(self,speed, color, name, is_police):
      self.speed = speed
      self.color = color
      self.name = name
      self.is_police = is_police

    def show_speed(self):
      return self.speed
  
    def move_(self, speed):
      self.speed = speed
      return self.speed
        
    def go(self, speed):
      print(f'{self.name} машина поехала, скорость {self.move_(speed)} км/ч')
        
    def stop(self):
      self.move_(0)
      print(f'{self.name} машина остановилась')
        
    def turn(self, direction):
      print(f'{self.name} машина повернула, направление: {direction}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
      super().__init__(speed, color, name, is_police)
  
    def show_speed(self):
      if self.speed > 60:
        print(f'{self.name} превышена разрешенная скорость движения 60 км/ч!')
      return self.speed

    
class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
      super().__init__(speed, color, name, is_police)

    
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
      super().__init__(speed, color, name, is_police)

    def show_speed(self):
      if self.speed > 40:
        print(f'{self.name} превышена разрешенная скорость движения 40 км/ч!')
      return self.speed

    
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
      super().__init__(speed, color, name, is_police)


car_police = PoliceCar(80, 'белый', 'Ford')
car_work = WorkCar(60, 'оранжевый', 'Камаз')
car_town = TownCar(79, 'желтый', 'volkswagen beetle')
car_sport = SportCar(200, 'красный', 'Ferrari')

car_work.show_speed()
car_police.show_speed()
car_town.show_speed()
car_sport.show_speed()
car_sport.go(300)
car_police.stop()