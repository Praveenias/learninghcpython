class TreeNode:
  def __init__(self,data):
    self.data = data
    self.children = []
    self.parent = None

  def add_child(self,child):
    child.parent = self
    self.children.append(child)

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level +=1
      p = p.parent
    return level
  
  def print_tree(self):
    children = self.children
    print('|__' * self.get_level()  + self.data)
    for child in children:
      child.print_tree()



def built_tree():
  nilupul = TreeNode("nilupul")
  chimay = TreeNode("chimay")
  vishwa = TreeNode('vishwa')
  dhaval = TreeNode('dhaval')
  abhijit = TreeNode('abhijit')
  nilupul.add_child(chimay)
  nilupul.add_child(vishwa)
  vishwa.add_child(dhaval)
  vishwa.add_child(abhijit)
  print(nilupul.print_tree())

if __name__ == '__main__':
  built_tree()


  
    