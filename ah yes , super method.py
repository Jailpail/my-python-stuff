class dadjoe:
  def __init__(self):
   super().__init__()
   self.years = input("give me your age: ")
class childjoe:
  def __init__(self):
   super().__init__()
   self.dateofbirth = input("give me your date of birth: ")
class reality(dadjoe, childjoe):
  def print_info(self):
   print(self.years)
   print(self.dateofbirth)
  def truthchecker(self):
    currentyear = 2022
    truthcheck = currentyear - self.years
    if truthcheck == self.dateofbirth:
             print("thanks for not lying")
    else:
             print("you dirty liar")
realjoe = reality()
realjoe.print_info()
realjoe.truthchecker()
