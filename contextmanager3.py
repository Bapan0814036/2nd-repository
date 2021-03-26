from contextlib import contextmanager

@contextmanager
def file_writer(name):
   try:
      m=open(name,'w')
      yield(m)
   finally:
      m.close()


if __name__=="__main__":
   with file_writer("hello200.txt") as p:
       p.write("hello23\n")
       p.write("hello24\n")
       p.write("hello25\n")