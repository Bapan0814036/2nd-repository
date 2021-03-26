class A:
   def __init__(self,name):
      self.name=name
   def __enter__(self):
      try:
        self.m=open(self.name,'w')
        return self.m
   def __exit__(self):
      print("Exiting the exit block")
      self.m.close()


if __name__=="__main__":
   with A("hello.txt") as a:
       print(a)
