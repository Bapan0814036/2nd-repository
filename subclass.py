class Base:
   pass

class Derived(Base):
   pass


if __name__=="__main__":
   print(issubclass(Derived,Base))
   print(issubclass(Base,Derived))
   d=Derived()
   b=Base()
   print(isinstance(b,Base))
   print(isinstance(d,Base))
   print(isinstance(b,Derived))
   print(isinstance(d,Derived))
