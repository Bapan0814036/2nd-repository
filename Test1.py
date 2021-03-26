class A:
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
