class TreeNode:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self,data):
    if data == self.data:
      return 
    
    if data < self.data:
      if not self.left:
        self.left = TreeNode(data)
      else:
        self.left.add_child(data)

    if data > self.data:
      if not self.right:
        self.right = TreeNode(data)
      else:
        self.right.add_child(data)
    
    return
  
def in_order(root):
  ele = []
  if root.left:
    ele += in_order(root.left)

  ele.append(root.data)

  if root.right:
    ele += in_order(root.right)

  return ele

def lca(root,n1,n2):
  # print(root.right.data)
  # return
  if root.left.data == n1 and root.right.data == n2:
    return root.data
  if root.left:
    lca(root.left,n1,n2)

  if root.right:
    lca(root.right,n1,n2)
  

if __name__ == '__main__':
  root = TreeNode(4)
  root.add_child(3)
  root.add_child(5)
  # root.add_child(5)

  # print(in_order(root))
  print(lca(root,3,5))