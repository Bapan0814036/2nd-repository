def fun(cls):
   print('Decorating {}'.format(cls.__name__))
   def wrapper(*args):
     return cls(*args)
   return wrapper

@fun
class A:
  def __init__(self,a,b):
     self.a=a
     self.b=b
  def func(self):
     print(fun.__name__)
  def __str__(self):
     return "{} is a and {} is b".format(self.a,self.b)

if __name__=="__main__":
   a=A(1,2)
   print(a)
   a.func()