#9_3
class Worker:
    def __init__(self, name, surname, position, income):
      self.name = name
      self.surname = surname
      self.position = position
      self._income = income
      self.dict_income = {
        50000: {"wage": 20000, "bonus": 30000},
        20000: {"wage": 10000, "bonus": 10000},
        10000: {"wage": 10000, "bonus": 0},
      }
      
  
class Position(Worker):
  def __init__(self, name, surname, position, income):
      super().__init__(name, surname, position, income)

  
  def get_full_name(self):
    return (self.name, self.surname)

    
  def get_total_income(self):
    return (f'оклад: {self.dict_income[self._income]["wage"]}, премия: {self.dict_income[self._income]["bonus"]}')


master = Position('Игорь', 'Иванов', 'Master', 20000)
worker = Position('Петр', 'Петров', 'Worker', 10000)
chief = Position('Дмитрий', 'Дмитриев', 'Chief', 50000)

print( master.get_full_name(), master.get_total_income())
print( worker.get_full_name(), worker.get_total_income())
print( chief.get_full_name(), chief.get_total_income())