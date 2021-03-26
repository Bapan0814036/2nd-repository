class A:
  def __init__(self,a):
     self.a=a
  def __str__(self):
    return "{} is the value of a".format(self.a)

class B:
  def __init__(self,b):
     self.b=b
  def __str__(self):
    return "{} is the value of b".format(self.b)

class C(A,B):
   def __init__(self,a,b):
      A.__init__(self,a)
      B.__init__(self,b)

   def __str__(self):
     return "{} is value of a {} is value of b".format(self.a,self.b)

class S(A):
  def __init__(self,a):
     super().__init__(a)


if __name__=="__main__":
   a=C(2,3)
   print(a.__dict__)
   print(a)
   s=S(31)
   print(s.__dict__)