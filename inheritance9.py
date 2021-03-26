class A:
  def __init__(self,a):
      print("A class executed")
      self.a=a
class B:
  def __init__(self,b):
      print("B class executed")
      self.b=b

class C(A,B):
   def __init__(self,a,b,c):
      print("C class executed")
      A.__init__(self,a)
      B.__init__(self,b)
      self.c=c

   def fun(self):
     self.m=2

if __name__=="__main__":
   c=C(1,2,3)
   print(c.__dict__)
   c.fun()
   print(c.__dict__)
   print("d object values")
   d=C(4,5,6)
   print(d.__dict__)

   

   