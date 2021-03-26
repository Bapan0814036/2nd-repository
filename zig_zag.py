class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
   def zig_zag(self):
       stack1=[]
       stack2=[]
       stack1.append(self)
       while stack1 or stack2:
           while stack1:
              s=stack1.pop(-1)
              print(s.value)
              if s.left:
                 stack2.append(s.left)
              if s.right:
                 stack2.append(s.right)
           while stack2:
              s=stack2.pop(-1)
              print(s.value)
              if s.right:
                 stack1.append(s.right)
              if s.left:
                 stack1.append(s.left)
              
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


if __name__=="__main__":
    node=Node(12)
    node.insert(9)
    node.insert(4)
    node.insert(10)
    node.insert(1)
    node.insert(5)
    node.insert(22)
    node.insert(14)
    node.insert(19)
    node.insert(25)
    node.zig_zag()
    