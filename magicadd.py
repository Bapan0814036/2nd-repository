class A:
  def __init__(self,a):
     self.a=a
  def __add__(self,other):
      if isinstance(other,A):
         return self.a+other.a

if __name__=="__main__":
   a=A(3)
   b=A(4)
   print(a+b)
