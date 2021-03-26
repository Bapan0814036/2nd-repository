class A:
  def __init__(self,name):
     self.name=name
  def __enter__(self):
     self.m=open(self.name,'w')
     return self.m
  def __exit__(self,exc_type,exc_test,exc_ten):
    if self.m:
       self.m.close()

if __name__=="__main__":
  with A("hello.txt") as a:
      a.write("Forward\n")
      a.write("Forward\n")
      a.write("Forward\n")