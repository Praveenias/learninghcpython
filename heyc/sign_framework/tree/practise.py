from collections import deque

class TreeNode():

  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def addChild(self,data):
    if self.data < data : 
      if self.right is None:
        self.right = TreeNode(data)
        return
      else:
        self.right.addChild(data)

    else : 
      if self.left is None:
        self.left = TreeNode(data)
        return
      else:
        self.left.addChild(data)

  def addMultipleChild(self,data1):
    for i in data1:
      self.addChild(i)

  def inorder(self):
    result = []
    if self.left:
      result += self.left.inorder()
    result.append(self.data)
    if self.right:
      result += self.right.inorder()
    return result

  def preorder(self):
    result = []
    result.append(self.data)
    if self.left:
      result += self.left.preorder()
   
    if self.right:
      result += self.right.preorder()
    return result
  
  def countLeaves(self):
    count = 0
    if self.left and self.right:
      count +=1
    if self.left:
      count += self.left.countLeaves()
    if self.right:
      count += self.right.countLeaves()

  def levelOrder(self):
    queue = deque([])
    queue.append(self)
    result = []
    while queue:
      dequee = queue.popleft()
      result.append(dequee.data)
      if dequee.left:
        queue.append(dequee.left)
      if dequee.right:
        queue.append(dequee.right)
    return result





    

if __name__ == "__main__":
  root = TreeNode(10)
  root.addChild(8)
  root.addMultipleChild([3,7,-1,12])
  #in_order = root.inorder()

  print(root.levelOrder())
  #print(in_order)

