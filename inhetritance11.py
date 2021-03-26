class A:
  def __init__(self,a,b):
     print("Base class executed")
     self.a=a
     self.b=b
  def __str__(self):
    return "{} and {}".format(self.a,self.b)

class C(A):
   def __init__(self,a,b):
     print("Parent class executed")
     super().__init__(a,b)
   def __str__(self):
     return "{} and {}".format(self.a,self.b)

if __name__=="__main__":
  a=C(2,4)
  print(a)
  
   