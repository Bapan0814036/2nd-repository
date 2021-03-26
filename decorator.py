from functools import wraps

def decorator(func):
   "decorator function"
   @wraps(func)
   def wrapper(*args):
     print("Inside wrapper")
     print("{}".format(fun.__name__))
   return wrapper

@decorator
def fun(*args):
  for i in args:
      print(i)

if __name__=="__main__":
   fun(1,2,3,4,5)
