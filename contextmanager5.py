class A:
   def __init__(self,name):
      self.name=name
   def __enter__(self):
      self.m=open(self.name,'w')
      return self.m
   def __exit__(self,exc_u,exc_v,exc_w):
     if self.m:
       self.m.close()

if __name__=="__main__":
   with A("hello100.txt") as f:
       f.write("hello hello\n")
       f.write("hello Bapan\n")
       f.write("hello gf\n")