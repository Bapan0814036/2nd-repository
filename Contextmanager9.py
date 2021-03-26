class B:
  def __init__(self,name):
     self.name=name
  def __enter__(self):
     self.m=open(self.name,'w')
     return self.m
  def __exit__(self,x,y,z):
     if self.m:
        self.m.close()
  def printt(self):
     self.m.write(' ')
     self.m.write('hello')


if __name__=="__main__":
   with B("testtest2.txt") as b:
       b.write("hello")