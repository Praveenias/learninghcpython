

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next =None
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self,nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for n in nodes:
                node.next = Node(data=n)
                node = node.next


    def addathead(self,data):
        if self.head is None:
            self.head = Node(data=data)
            return

        node = Node(data=data)
        node.next = self.head
        self.head  = node
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def addatend(self,data):
        if self.head is None:
            self.head = Node(data=data)
            return
        for cur in self:
            pass
        cur.next = Node(data=data)
    def addatindexval(self,index,val):
        node = self.head
        while node is not None:
            if node.data == index:
                nodei = Node(data=val)
                nodei.next = node.next
                node.next = nodei
            node = node.next
            
    def totalcount(self):
        count = 0
        for i in self:
            count+=1
        return count

    def addatindex(self,index,val):
        if index > self.totalcount():
            raise Exception("No value for that index val")

        for cou,i in enumerate(self,start=1):
            if cou == index-1:
                node = Node(data=val)
                node.next = i.next
                i.next = node
    
    def get_middle_element(self):
        middle = self.totalcount()//2
        for ind,i in enumerate(self):
            if ind == middle:
                print("middle : ",i.data)

    def removematchelement(self,val):
        node = self.head
        if node.data == val:
            self.head = self.head.next
        previous_node = self.head
        for node in self:
            if node.data == val:
                previous_node.next = node.next
                continue
            previous_node = node



if __name__ == '__main__':
    ll = LinkedList(["2","2","2","2","2"])
    #ll.addathead("2")
    # ll.addathead("1")
    # ll.addatend("3")
    # ll.addatindexval("3","3.5")
    # ll.addatindex(4,"1.5")
    #print(ll.totalcount())
    #ll.get_middle_element()
    ll.removematchelement("2")
    print(ll)
