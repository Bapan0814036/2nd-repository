class A:
  def __init__(self,a):
     self.a=a
  def __add__(self,other):
     if isinstance(other,A):
       return other.a+self.a
     elif isinstance(other,int):
       return self.a+other
     else:
       return self.a
  def __repr__(self):
     return f'{self.a} is a'

class B:
   def __init__(self,b):
      self.b=b
   def __repr__(self):
      return f'{self.b} is value'

if __name__=="__main__":
   a=A(23)
   print(a)
   b=B(34)
   print(b)
   c=A(33)
   print(a+c)#56
   print(a+1)#24
   print(a+b)#23