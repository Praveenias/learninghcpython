class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        pass


    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(data=val)
            return
        node = Node(data=val)
        node.next = self.head
        self.head = node
        
        

    def addAtTail(self, val: int) -> None:
        pass
        

    def addAtIndex(self, index: int, val: int) -> None:
        pass
        

    def deleteAtIndex(self, index: int) -> None:
        pass
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(10)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)