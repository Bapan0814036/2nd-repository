class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __iter__(self):
     print("Iterator Executed")
     self.a=10
     self.b=0
     return self
  def __str__(self):
     return "{} is a {} is b".format(self.a,self.b)

  def __next__(self):
    if self.b<self.a:
      item=self.b
      self.b=self.b+1
      return item
    else:
       raise StopIteration   


if __name__=="__main__":
  a=A(5,0)
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a))
  print(next(a)) 
  print(next(a))
  print(next(a))
  