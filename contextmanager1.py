class A:
  def __init__(self,name):
     self.name=name
  def __enter__(self):
     self.m=open(self.name,'w')
     return self.m
  def __exit__(self,ex_t,ex_u,ex_v):
     if self.m:
        self.m.close()

if __name__=="__main__":
   with A("hello10.txt") as f:
       f.write("Hello Everybody")
       f.write("Hello Guys")
       f.write("Hello")


