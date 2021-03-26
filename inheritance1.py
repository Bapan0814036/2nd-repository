class Base1:
   def __init__(self):
     self.str1="Geeks1"

class Base2:
   def __init__(self):
     self.str2="Geeks2"


class Derived(Base1,Base2):
   def __init__(self):
     Base1.__init__(self)
     Base2.__init__(self)
   def printstr(self):
      print(self.str1,self.str2)

 
if __name__=="__main__":
   d=Derived()
   d.printstr()
   
