l=[[1,2,10],[4,5,1],[7,8,0],[11,12,1]]

def getkey(m):
  return m[2]

class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __repr__(self):
      return f"({self.a},{self.b})"

m=[A(0,3),A(1,2),A(5,6),A(2,5)]

if __name__=="__main__":
    print(sorted(l,key=getkey))
    print(sorted(m,key=lambda obj:obj.b))
    