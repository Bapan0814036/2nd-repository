class Node:
   def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None
   def insert(self,value):
      if not self:
        self.value=value
      else:
          if self.value>value:
             if self.left:
                self.left.insert(value)
             else:
                self.left=Node(value)
          elif self.value<value:
             if self.right:
                self.right.insert(value)
             else:
                self.right=Node(value)
          else:
             print("Duplication not allowed")
   def lvl_order(self):
      queue=[]
      queue.append(self)
      while queue:
         s=queue.pop(0)
         print(s.value)
         if s.left:
            queue.append(s.left)
         if s.right:
            queue.append(s.right)

   def height(self,k):
      queue=[]
      queue.append(self)
      len_queue=0
      count=0
      while queue:
        len_queue=len(queue)
        if len_queue:
           count=count+1
        else:
           break
        while len_queue:
            s=queue.pop(0)
            if s.left:
              queue.append(s.left)
            if s.right:
              queue.append(s.right)
            len_queue=len_queue-1
        if count==k:
          while queue:
             print(queue.pop(0).value)
      
if __name__=="__main__":
  node=Node(12)
  node.insert(17)
  node.insert(22)
  node.insert(14)
  node.insert(25)
  node.insert(9)
  node.insert(4)
  node.insert(7)
  node.insert(10)
  node.insert(11)
  print("The level order traversal of the tree")
  node.lvl_order()
  print("The height of the binary tree is")
  node.height(3)