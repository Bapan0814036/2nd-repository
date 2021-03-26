class MyClass:
   __var=2
   def __init__(self,a,b):
      self.a=a
      self.b=b
      self.__test=4

   def __str__(self):
      return "{} is value of a {} value of b".format(self.a,self.b)


   def __hello(self):
      print("Hello method executed")


class Test:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __str__(self):
      return "{} is a {} is b".format(self.a,self.b)
   def __repr__(self):
      return "{} is a {} is b in repr".format(self.a,self.b)


if __name__=="__main__":
   m=MyClass(2,3)
   print(m)
   print(m._MyClass__test)
   print(m._MyClass__var)
   print(m.__dict__)
   m._MyClass__hello()
   t=Test(4,5)
   print(t)
   print([t])
   