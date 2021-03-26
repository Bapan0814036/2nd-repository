class Pet:
  def __init__(self,*args):
     print("Pet class executed")
     self.name=args[0]
     self.age=args[1]
  def __str__(self):
     return "{} is name {} is age Pet class".format(self.name,self.age)
class Cat(Pet):
    def __init__(self,*args):
       print("Cat class executed")
       super().__init__(*args)
       self.color=args[2]
    def __str__(self):
       return "{} is name {} is age Cat class".format(self.name,self.age)

def main():
   p=Pet("Pet",21)
   c=Cat("Cat",32,"Red")
   print(p)
   print(c)
   print(c.__dict__)


if __name__=="__main__":
   main()
   p=Pet("Pet",21)
   c=Cat("Cat",32,"White")
   print(p)
   print(isinstance(p,Pet))
   print(isinstance(c,Cat))
   print(isinstance(p,Cat))
   print(isinstance(c,Pet))
   print(c)
   print(c.__dict__)
   
   
   