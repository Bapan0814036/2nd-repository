class Base:
   def __init__(self,x):
      self.x=x
   def __str__(self):
      return str(self.x)

class Derived(Base):
    def __init__(self,x,y):
       self.x=x
       self.y=y

    def __str__(self):
       return str(self.y)+'   '+str(self.x)

if __name__=="__main__":
    b=Base(2)
    print(b)
    d=Derived(2,3)
    print(d.__dir__)
    print(d)



