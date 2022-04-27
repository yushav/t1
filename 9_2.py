#9_2
class Road:
    def __init__(self, length, width):
      self._length = length
      self._width = width
      
  
    def mass_asphalt(self, thick, mass_m2_cm):
      return self._length * self._width * mass_m2_cm * thick


road_2022 = Road(5000, 20)
print(road_2022.mass_asphalt(5, 25))