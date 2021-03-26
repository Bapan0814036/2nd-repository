class A:
  def __init__(self,name):
     self.name=name
  def __enter__(self):
     self.m=open(self.name,'w')
     return self.m
  def __exit__(self,exc_type,exc_val,exc_tb):
    if self.m:
     self.m.close()

if __name__=="__main__":
   with A("hello1.txt") as e:
      e.write("Hello1\n")
      e.write("Hello2\n")
      e.write("hellohello\n")
      
