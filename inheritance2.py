class Base:
   def __init__(self,x):
      self.x=x
class Derived(Base):
   def __init__(self,x,y):
      Base.x=x
      self.y=y
   def printXY(self):
      print(Base.x,self.y)


if __name__=="__main__":
   d=Derived(2,3)
   d.printXY()
   print(d.__dict__)
   if issubclass(Derived,Base):
      print(True)
   else:
      print(False)