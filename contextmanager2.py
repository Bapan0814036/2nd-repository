from contextlib import contextmanager

@contextmanager
def cmanager(name):
   try:
      c=open(name,'w')
      yield(c)
   finally:
      c.close()


if __name__=="__main__":
   file=input("Enter file name")
   with cmanager(file) as cm:
      cm.write("Hello200\n")
      cm.write("Hello300\n")
      cm.write("Hello400\n")
      print("Exiting with")

