class Person:
   str1="Hello"
   def __init__(self,name):
      self.name=name
   def say_hi(self):
      print("Hello my name is bapan")


if __name__=="__main__":
   p=Person("Hello100")
   p.say_hi()
   Person.say_hi(p)
   print(p.__dict__)
   print(Person.str1)