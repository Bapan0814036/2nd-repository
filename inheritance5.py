class X:
  def __init__(self,a):
     self.num=a
  def doubleup(self):
     self.num*=2

class Y(X):
  def __init__(self,a):
     X.__init__(self,a)
  def tripleup(self):
     self.num*=3

if __name__=="__main__":
  obj=Y(4)
  print(obj.num)
  obj.doubleup()
  print(obj.num)
  obj.tripleup()
  print(obj.num)
