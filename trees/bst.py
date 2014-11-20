# binary search tree implementation

class Node:
        def __init__(self, key, val):
                self.key = key
                self.val = val
                self.left = None
                self.right = None


def insert(x, key, val):
        if (x == None): return Node(key, val)

        if (key < x.key):
                x.left = insert(x.left, key, val)
        elif (key > x.key):
                x.right = insert(x.right, key, val)
        else:
                x.val = val

        return x


def get(x, key):
        while (x != None):
                if (key < x.key):
                        x = x.left
                elif (key > x.key):
                        x = x.right
                else:
                     return x.val

        return None


root = Node(5, 'e')
insert(root, 6, 'f')
insert(root, 3, 'c')
insert(root, 7, 'g')
insert(root, 4, 'd')
insert(root, 10, 'j')
insert(root, 2, 'b')

a = get(root, 3)
        
print(a)


