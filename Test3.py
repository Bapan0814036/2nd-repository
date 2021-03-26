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
        def postorder(self):
           stack1=[]
           stack2=[]
           stack1.append(self)
           while stack1:
             s=stack1.pop()
             stack2.append(self)
             if s.left:
                stack1.append(s.left)
             if s.right:
                stack1.append(s.right)
             
        def preorder(self):
          stack=[]
          stack.append(self)
          while stack:
             s=stack.pop()
             print(s.value)
             if s.left:
               stack.append(s.left)
             if s.right:
               stack.append(s.right)
    
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
                test=test.right
              else:
                break
    
    if __name__=="__main__":
        node=Node(12)
        node.insert(17)
        node.insert(14)
        node.insert(23)
        node.insert(20)
        node.insert(25)
        node.insert(9)
        node.insert(4)
        node.insert(11)
        print("The inorder traversal of the graph:")
        node.inorder()
        print("The preorder traversal of the graph:")
        node.preorder()