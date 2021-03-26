class A:
  def __init__(self,a):
      self.a=a
  def __str__(self):
     return "{} is the value of a".format(self.a)

class B:
  def __init__(self,b,c):
     self.b=b
     self.c=c
  def __str__(self):
    return "{} is b {} is c".format(self.b,self.c)

class C(A):
   def __init__(self,a):
     super().__init__(a)
   def __str__(self):
      return "{} is value of a".format(self.a)


class D(A,B):
   def __init__(self,a,b,c,d):
      A.__init__(self,a)
      B.__init__(self,b,c)
      self.d=d

   def __str__(self):
     return "{} is a {} is b {} is c {} is d".format(self.a,self.b,self.c,self.d)

if __name__=="__main__":
  c=C(2)
  print(c)
  d=D(1,2,3,4)
  print(d)




   
