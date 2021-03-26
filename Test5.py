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
   def tree_view(self,right):
       self.level_trav(right)
      
   def level_trav(self,right):
       queue=[]
       queue_len=0
       count=0
       if self:
          queue.append(self)
          print(queue[0].value)
       while queue:
            queue_len=len(queue)
            if queue_len:
               count=count+1
            while queue_len:
               s=queue.pop(0)
               if s.left:
                  queue.append(s.left)
               if s.right:
                  queue.append(s.right)
               queue_len=queue_len-1
            
            if queue:
               if right:
                 print(queue[0].value)
               else:
                 print(queue[-1].value)


if __name__=="__main__":
   node=Node(12)
   node.insert(9)
   node.insert(10)
   node.insert(11)
   node.insert(4)
   node.insert(23)
   node.insert(14)
   node.insert(17)
   node.insert(29)
   node.insert(25)
   print("Right view of the tree is")
   node.tree_view(True)
   print("Left view of the tree is")
   node.tree_view(False)
            