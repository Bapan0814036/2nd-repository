class A:
  def __new__(cls,*args,**kwargs):
     print("new method executed")
     return object.__new__(cls)
  def __init__(self,a,b):
     print("Init method executed")
     self.a=a
     self.b=b
  def __str__(self):
     return "{} is a {} is b".format(self.a,self.b)

if __name__=="__main__":
   a=A(1,2)
   print(a)
