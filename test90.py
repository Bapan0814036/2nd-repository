def meta_cls(classname,baseclass,attr):
    nattr={'mod'+key:attr[key] for key in attr}
    def fun(self,a,b):
       self.a=a
       self.b=b
    nattr['__call__']=fun
    return type(classname,baseclass,nattr)

Mymeta=meta_cls

class A(metaclass=Mymeta):
   def __init__(self):
      print("init executed")
   def seta(self,a):
      self.a=a
   def geta(self):
      return self.a

if __name__=="__main__":
   m=A()
   print(m.modseta(4))
   print(m.modgeta())
