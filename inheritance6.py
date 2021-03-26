class Person:
  def __init__(self,name):
     self.name=name
  def getName(self):
     return self.name
  def isEmployee(self):
     return False

class Employee(Person):
   def __init__(self,name,id):
     super().__init__(name)
     self.empid=id

   def isEmployee(self):
       return True
   def getid(self):
       return self.empid

if __name__=="__main__":
   emp=Employee("Geek1","Geek2")
   print(emp.getName())
   print(emp.isEmployee())
   print(emp.getid())

      
