from collections import defaultdict
class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None
      self.id=0
   def vertical_order(self):
      m=defaultdict(list)
      queue=[]
      queue.append(self)
      while queue:
         s=queue.pop(0)
         if s.id not in m:
            m[s.id]=[]
            m[s.id].append(s.value)
         else:
            m[s.id].append(s.value)
         if s.left:
           queue.append(s.left)
         if s.right:
           queue.append(s.right)
      print("The top view of the tree is")
      for i in sorted(m.keys()):
        print(m[i][0])
      print("The bottom view of the tree is")
      for i in sorted(m.keys()):
        print(m[i][-1])
        
      

   def insert(self,value):
      if not self:
         self.value=value
      else:
         if self.value>value:
            if self.left:
               self.left.insert(value)
            else:
               self.left=Node(value)
               self.left.id=self.id-1
         elif self.value<value:
            if self.right:
               self.right.insert(value)
            else:
               self.right=Node(value)
               self.right.id=self.id+1
         else:
            print("Duplication Not Allowed")

if __name__=="__main__":
   node=Node(14)
   node.insert(9)
   node.insert(6)
   node.insert(12)
   node.insert(4)
   node.insert(7)
   node.insert(23)
   node.insert(18)
   node.insert(27)
   node.insert(24)
   node.vertical_order()


