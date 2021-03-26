 class MyClass:
   number=0
   name="Hello"

   def __init__(self):
      self.a=0

   def __repr__(self):
     return MyClass.name+' '+str(MyClass.number)

   def set_a(self,b):
      self.a=b

   @property
   def set_number(self):
      return MyClass.number

   @set_number.setter
   def set_number(self,a):
      MyClass.number=a

   def __add__(self,other):
     if isinstance(other,MyClass):
        self.a=other.a+self.a
     return self.a

def main():
  m=MyClass()
  print(m.number)
  print(MyClass.number)
  print(m.name)
  print(MyClass.name)

if __name__=="__main__":
  main()
  print(dir(MyClass))
  print(MyClass.__module__)
  n=MyClass()
  print(n.__dict__)
  n.set_a(2)
  o=MyClass()
  o.set_a(3)
  print(n)
  n.set_number=36
  print(MyClass.number)
  print(n)
  print(n+o)
  
  