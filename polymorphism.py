class Person:
   def __init__(self,name):
      self.name=name
   def getName(self):
      return self.name
   def isEmployee(self):
      return False

class Employee(Person):
   def isEmployee(self):
      return True

if __name__=="__main__":
   p=Person("Hello")
   print(p.getName())
   print(p.isEmployee())
   print(p.__dict__)
   e=Employee("Geek")
   print(e.getName())
   print(e.isEmployee())
   print(e.__dict__)


