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


    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

tree = Node(10)
tree.insert(3)
tree.insert(12)
tree.insert(22)
tree.insert(17)
tree.insert(55)
tree.insert(0)
tree.insert(1)
tree.print_tree()
print "Tree height is {0}".format(tree.height(tree))
