class A:
  number=2
  def __init__(self,a):
    self.a=a
  @property
  def set_a(self):
     return self.a
  @set_a.setter
  def set_a(self,value):
     self.a=value
  def __repr__(self):
     return f'{self.a} is value'

if __name__=="__main__":
   a=A(3)
   print(a)
   print(a.__dict__)
   a.set_a=5
   print(a)
   print(a.__dict__)
   print(A.number)
   print(a.__dict__)
   a.number=7
   print(a.__dict__)
   b=A(4)
   print(b)
   print(b.__dict__)

