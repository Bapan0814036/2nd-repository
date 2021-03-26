class A:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def __call__(self,fun):
    print("Executing Call")
    def wrapper(*args):
       print("Inside wrapper")
       return fun(*args)
    return wrapper

@A(2,3)
def function1(*args):
   print("Inside function {}".format(args[0]))
   print("Inside function {}".format(args[1]))
   print("Inside function {}".format(args[2]))


if __name__=="__main__":
  function1(2,3,4)