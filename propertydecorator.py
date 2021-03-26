class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   @property
   def set_a(self):
     return self.a
   @set_a.setter
   def set_a(self,a):
       self.a=a
   @property
   def set_b(self):
      return self.b
   @set_b.setter
   def set_b(self,b):
      self.b=b

if __name__=="__main__":
   a=A(2,3)
   print(a.__dict__)
   print(a.set_a)
   a.set_a=12
   print(a.__dict__)
   print(a.set_b)
   a.set_b=24
