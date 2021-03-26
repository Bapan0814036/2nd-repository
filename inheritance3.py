class A:
  def __init__(self,x):
     print("Base constructor executed")
     self.x=x
  def __str__(self):
     return str(self.x)

class B(A):
   def __init__(self,x,y):
      super().__init__(x)
      self.y=y
   def __str__(self):
     return "{} is x {} is y".format(self.x,self.y)

if __name__=="__main__":
   a=B(2,3)
   print(a)
   