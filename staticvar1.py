class A:
   var="hello"
   def __init__(self,a):
     self.a=a
   

if __name__=="__main__":
   a=A(12)
   print(a.__dict__)
   print(a.var)
   print(a.__dict__)
   a.var=24
   print(a.__dict__)
   print(A.var)