class A:
  test=0
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __add__(self,other):
     if isinstance(other,A):
        return other.a+self.a
     elif isinstance(other,int):
        return other+self.a
     else:
        return -1
     
if __name__=="__main__":
   d=A(2,3)
   print(A.test)
   A.test=5
   print(A.test)
   print(d.test)
   print(d.__dict__)
   d.test=5
   print(d.__dict__)
   print(d+1)
   print(d+7)
   m=A(5,6)
   print(m.__dict__)
   m.test1=4
   print(m.__dict__)
   print(m+'a')