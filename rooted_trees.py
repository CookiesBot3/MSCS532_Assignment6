class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

if __name__ == '__main__':
    # Example usage
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root.add_child(child1)
    root.add_child(child2)
