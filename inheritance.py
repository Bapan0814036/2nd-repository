class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __str__(self):
    return "{} is a {} is b".format(self.a,self.b)

class B:
  def __init__(self,c,d):
     self.c=c
     self.d=d
  def __str__(self):
    return  "{} is c {} is d".format(self.c,self.d)

class C(A,B):
  def __init__(self,a,b,c,d,e):
     A.__init__(self,a,b)
     B.__init__(self,c,d)
     self.e=e
  def __str__(self):
    return "{} is a {} is b {} is c {} is d {} is e".format(self.a,self.b,self.c,self.d,self.e)

if __name__=="__main__":
  m=C(1,2,3,4,5)
  print(m)