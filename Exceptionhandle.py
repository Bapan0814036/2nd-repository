class A(Exception):
   def __init__(self,name):
      self.name=name
   def __str__(self):
      return "{} is the exception occured".format(self.name)

if __name__=="__main__":
   try:
     raise A("Value error ")
   except Exception as e:
     print(e)