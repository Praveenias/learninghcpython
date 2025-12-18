from collections import deque
class TreeNode:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self,data):
    if self.data == data:
      return
    
    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = TreeNode(data)

    if data > self.data:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = TreeNode(data)
    
    return
  
  def inorder(self):
    element = []
    if self.left:
      element += self.left.inorder()
    element.append(self.data)
    if self.right:
      element += self.right.inorder()
    return element
  
  def preorder(self):
    element = []
    element.append(self.data)
    if self.left:
      element += self.left.preorder()
    
    if self.right:
      element += self.right.preorder()
    return element
  def postorder(self):
    element = []
    
    if self.left:
      element += self.left.postorder()
    
    if self.right:
      element += self.right.postorder()
    element.append(self.data)
    return element
  
  def height(self):
    height = 1
    if self.right:
      height += self.right.height()

    return height
  
  def level_order(self):

    result = []
    queue = deque([self])
    while queue:
      ele = queue.popleft()
      result.append(ele.data)
      if ele.left:
        queue.append(ele.left)
      if ele.right:
        queue.append(ele.right)

    return result

  
def leaf_mode(node):
  if not node:
    return 0
  if not node.left and not node.right:
    return 1
  
  return leaf_mode(node.left) + leaf_mode(node.right)

def checkSymmentric(self,left,right) ->bool:
  if not left and not right:
      return True
  if not left or not right:
      return False
  if left.val != right.val:
      return False
  return self.checkSymmentric(left.left,right.left) and self.checkSymmentric(left.right,right.right)

if __name__ == '__main__':
  head = TreeNode(5)
  head.add_child(2)
  head.add_child(10)
  head.add_child(1)
  head.add_child(3)
  head.add_child(15)
  print(head.inorder())
  print(head.preorder())
  print(head.height())
  print(leaf_mode(head))
  print(head.level_order())


