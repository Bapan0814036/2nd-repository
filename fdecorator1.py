def fun(cls):
  def wrapper(*args):
    def average(cls,x,y):
       return (x+y)/2
    setattr(cls,'average',average)
    return cls(*args)
  return wrapper

@fun
class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def __str__(self):
     return "{} and {}".format(self.a,self.b)


if __name__=="__main__":
   a=A(2,3)
   print(a)
   print(a.average(4,6))