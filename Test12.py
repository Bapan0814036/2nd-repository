class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None
   def insert(self,value):
      if not self:
         self.value=value
      elif self.value>value:
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
   def postorder(self):
      stack1=[]
      stack2=[]
      stack1.append(self)
      while stack1:
        s=stack1.pop()
        stack2.append(s)
        if s.left:
           stack1.append(s.left)
        if s.right:
           stack1.append(s.right)
      while stack2:
        print(stack2.pop().value)

   def preorder(self):
       stack=[]
       if not self:
         print("Can traverse the tree")
       else:
          stack.append(self)
          while stack:
            s=stack.pop()
            print(s.value)
            if s.right:
              stack.append(s.right)
            if s.left:
              stack.append(s.left)  
   def inorder(self):
      stack=[]
      test=self
      while True:
          if test:
             stack.append(test)
             test=test.left
          elif stack:
              s=stack.pop()
              print(s.value)
              test=s.right
          else:
              break
if __name__=="__main__":
    node=Node(12)
    node.insert(7)
    node.insert(3)
    node.insert(10)
    node.insert(9)
    node.insert(17)
    node.insert(14)
    node.insert(22)
    node.insert(19)
    node.insert(25)
    print("Inorder traversal of the tree")
    node.inorder()
    print("Preorder traversal of the tree")
    node.preorder()
    print("Post order traversal of the tree")
    node.postorder()


