from contextlib import contextmanager

@contextmanager
def manage_file(name):
  try:
    m=open(name,'w')
    yield(m)
  finally:
    m.close()

if __name__=="__main__":
   with manage_file("test.txt") as f:
       f.write("hello\n")
       f.write("hello1\n")