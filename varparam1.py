def fun(**kwargs):
   print("The value of kwargs")
   print(kwargs["a"])
   print(kwargs["b"])

def fun1(*args):
   print("The value of args")
   for i in args:
     print(i)


if __name__=="__main__":
   fun(**{"a":1,"b":2})
   fun1(*(1,2,3))
   m=fun
   n=fun1
   m(**{"a":21,"b":22})
   n(*(1,2,3))