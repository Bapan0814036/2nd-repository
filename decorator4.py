def decorator(*args,**kwargs):
    def inner(func):
        print(kwargs['like'])
        return func
    return inner

@decorator(like="hello")
def func():
   print("Inside func")

if __name__=="__main__":
   func()
