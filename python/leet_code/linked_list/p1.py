class Node:
  def __init__(self,val,next=None) -> None:
    self.val = val
    self.next = next
  def __repr__(self) -> str:
    return "Value : "+str(self.val) + "  NEXT : "+str(self.next)
  

class LinkedList:
  def __init__(self) -> None:
    self.head = None
    
  def add_at_beginning(self,value):
    if self.head is None:
      self.head = Node(value)
      return
    node = Node(value,self.head)
    self.head = node
  
  def insert_value_end(self,value):
    if self.head is None:
      self.head = Node(value,None)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(value,None)

  def get_length(self):
    count=0
    itr=self.head
    while itr:
      count+=1
      itr = itr.next
    print(count)

    
  def print_ll(self):
    if self.head is None:
      return "no values found"
    itr = self.head
    value=""
    while itr:
        value += str(itr.val) if itr.next == None else str(itr.val)+"-->"
        itr =  itr.next
    print(value)
      


    
if __name__=='__main__':
  ll = LinkedList()
  ll.add_at_beginning(1)
  ll.add_at_beginning(0)
  ll.insert_value_end(2)
  ll.print_ll()
  ll.get_length()
