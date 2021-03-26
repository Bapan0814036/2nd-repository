from functools import wraps

def decorate(func):
  @wraps(func)
  def wrapper(*args):
    print("Executing lines")
    func(*args)
    print("Execution over")
    return
  return wrapper

@decorate
def fun1(str):
   print(str)

if __name__=="__main__":
  fun1("Hello")
  fun1("Welcome")