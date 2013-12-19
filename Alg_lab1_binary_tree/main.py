class Node:
    def __init__(self, data):
        """
        Tree node
        """
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        """
        Insert node in to tree
        """

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()


tree = Node(10)
tree.insert(3)
tree.insert(12)
tree.insert(2)
tree.print_tree()

