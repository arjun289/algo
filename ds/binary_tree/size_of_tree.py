
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class Tree:
    def __init__(self):
        root = None

def tree_size(root):
    if root is None:
       return 0
    else:
        return tree_size(root.left) +  tree_size(root.right) + 1



if __name__ == "__main__":
    n = Node(1)
    m = Node(2)
    o = Node(3)
    p = Node(4)
    q = Node(5)
   
    n.left = m
    n.right =o
    m.left = p
    m.right = q
    s = tree_size(n)
    print(s)

