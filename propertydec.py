class A:
   def __init__(self,a):
      self.a=a
      self.b={"test":'',"test1":''}
   @property
   def seta(self):
      return self.a
   @seta.setter
   def seta(self,a):
      self.a=a
   @property
   def setb(self):
      return self.b
   @setb.setter
   def setb(self,key):
      self.b["test"]=key["test"]
      self.b["test1"]="%2c".join(key["test1"])
   def display(self):
     print(f"{self.a} and {self.b} is the value")

if __name__=="__main__":
   m=A(2)
   print(m.seta)
   print(m.setb)
   m.seta=2
   m.setb={"test":3,"test1":['a','b']}
   m.display()
