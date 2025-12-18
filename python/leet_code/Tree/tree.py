class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def __str__(self) -> str:
        return self.data
    
    def __repr__(self) -> str:
        return self.data
    
    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

def built_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    tv = TreeNode("tv")


    laptop.add_child(TreeNode("dell"))
    laptop.add_child(TreeNode("lenovo"))

    tv.add_child(TreeNode("sony"))
    tv.add_child(TreeNode("vu"))

    
    root.add_child(laptop)
    root.add_child(tv)
    return root


if __name__ == '__main__':
    root = built_tree()
    root.print_tree()
