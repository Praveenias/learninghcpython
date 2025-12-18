class Queue:
  def __init__(self,capacity):
    self.left = -1
    self.right = -1
    self.capacity = capacity
    self.queuet = []

  def insert(self,data):
    if self.right > self.capacity:
      return 0
    self.queuet.append(data)
    self.right +=1

  def remove(self):
    print(self.left)
    if self.left == -1 or self.right < self.left:
      return 0
    self.left +=1
    print(self.left)
    return self.queuet[self.left]
  
  def size(self):
    return self.right - self.left +1
  
  def isEmpty(self):
    return self.size() == 0

  def traverse(self):
    self.left = 0 if self.left == -1 else self.left
    for i in range(self.left,self.right +1):
      print(self.queuet[i],end = '->')
    print()
  
if __name__ == '__main__':
  q = Queue(3)
  q.insert(1)
  print(q.left)
  # q.insert(2)
  # q.insert(3)
  # q.traverse()
  # print(q.size())
  # print(q.isEmpty())
  # q.remove()
  # q.traverse()
  # q.remove()
  q.remove()
  print(q.size())



