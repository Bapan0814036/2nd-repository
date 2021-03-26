class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __call__(self,func):
      def wrapper(*args):
         print("Executing1")
         return func(*args)
      return wrapper

@A(2,3)
def fun(*args):
  for i in args:
     print(i)

if __name__=="__main__":
   fun(1,2,3,4)