class Test:
   "This is a sample class"
   name="Hello"
   def fun(self):
     print("Hello")
   @classmethod
   def fun2(cls):
     print(Test.name)
   def fun1(self):
      print("This is second function")

if __name__=="__main__":
   t=Test()
   t.fun()
   print(Test.__dict__)
   print(Test.__doc__)
   Test.fun2()
   Test.fun(t)
   Test.fun1(t)