from datetime import date

class Person:
   def __init__(self,name,age):
       self.name=name
       self.age=age
   @classmethod
   def fromBirthDay(cls,name,year):
       return cls(name,date.today().year-year)

   @staticmethod
   def isAdult(age):
       return age>18


if __name__=="__main__":
   person1=Person("Mayank",21)
   person2=Person.fromBirthDay("Mayank",1996)
   print(person1.age)
   print(person2.age)
   print(Person.isAdult(22))
