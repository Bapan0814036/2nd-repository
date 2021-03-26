class A:
  def __new__(cls,*args,**kwargs):
     print("New method executed")
     return object.__new__(cls)

  def __init__(self,*args,**kwargs):
      print("Init method executed")
      self.a=args[0]
      self.b=args[1]

if __name__=="__main__":
   a=A(4,5,6)
   print(a.__dict__)