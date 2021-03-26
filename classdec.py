class A:
  def __init__(self,a):
    self.a=a
  def __call__(self,fun,*args):
    def fun1(*args):
       print("Executing 1")
       return fun(*args)
    return fun1

@A(2)
def fun1(*args):
   print(args[0])
   print(args[1])
   print(args[2])

if __name__=="__main__":
  fun1(1,2,3)
