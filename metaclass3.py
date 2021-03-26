class A:
  def __init__(self,data):
     self.data=data
  def getd3(self):
     return self.data*3

class Mymeta(type):
  def __new__(metaname,classname,baseclass,attrs):
     attrs['getdata']=A.__dict__['getd3']
     return type.__new__(metaname,classname,baseclass,attrs)
  def __init__(classobject,classname,baseclass,attrs):
     pass

class Kls(metaclass=Mymeta):
   def __init__(self,data):
      self.data=data
   def printd(self):
      print(self.data)
if __name__=="__main__":
   ik=Kls('Arun')
   ik.printd()
   print(ik.getdata())