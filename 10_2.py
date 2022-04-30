#10_2
from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def textile_comsum(self):
      pass    


class Coat(Clothes):
  def __init__(self, name, size):
    self.name = name
    self.size = size
    
  @property
  def textile_comsum(self):
    return self.size / 6.5 + 0.5


class Suit(Clothes):
  def __init__(self, name, height):
    self.name = name
    self.height = height

  @property
  def textile_comsum(self):
    return 2 * self.height + 0.3


red_coat = Coat( 'Red Coat', 36)
blue_suit = Suit( 'Blue Suit', 1.68)

print(red_coat.name, red_coat.textile_comsum)
print(blue_suit.name, blue_suit.textile_comsum)