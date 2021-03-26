class MyClass:
   def __init__(self,a):
     self.a=a
   def __add__(self,other):
      if isinstance(other,MyClass):
         b=self.a+other.a
         return MyClass(b)

   def __radd__(self,other):
      if other==0:
        return self
      else:
        return self.__add__(other)
   def __repr__(self):
      return "{} is value of a".format(self.a)

if __name__=="__main__":
   a=MyClass(2)
   b=MyClass(3)
   print(a+b)
   c=MyClass(4)
   print(sum([a,b,c]))
   print(dir(c))
   if hasattr(c,'a'):
     print("The object c has attribute a")
   setattr(c,'b',3)
   print(c.__dict__)
   setattr(c,'l',4)
   print(c.__dict__)


      