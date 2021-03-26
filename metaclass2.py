class C:
  def __init__(self,a):
     self.a=a
  def geta(self):
     return self.a

class B(type):
   def __new__(cls,classname,baseclass,attrs):
     attrs['geta']=C.__dict__['geta']
     return type.__new__(cls,classname,baseclass,attrs)
   def __init__(self,classname,baseclass,attrs):
            pass

class C(metaclass=B):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
       return "{} and {}".format(self.a,self.b)

if __name__=="__main__":
   c=C(9,2)
   print(c)
   print(c.geta())