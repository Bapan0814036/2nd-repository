def fun(*args):
   str1=''
   print(args)
   for i in args:
     str1+=str(i)
   print(str1)

def fun1(*args):
  print(args)

def funn(**kwargs):
   print(kwargs)

if __name__=="__main__":
   fun(1,2,3)
   fun1(*(1,2,3))
   funn(**{"a":1,"b":2})
