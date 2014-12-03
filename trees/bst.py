# binary search tree implementation

class Node:
        def __init__(self, key, val):
                self.key = key
                self.val = val
                self.left = None
                self.right = None
                self.count = 1


def insert(x, key, val):
        if (x == None): return Node(key, val)

        if (key < x.key):
                x.left = insert(x.left, key, val)
        elif (key > x.key):
                x.right = insert(x.right, key, val)
        else:
                x.val = val
        x.count = 1 + size(x.left) + size(x.right)

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


def floor(x, key):
        if (x == None): return None

        if (key == x.key): return x.key

        if (key < x.key): return floor(x.left, key)

        t = floor(x.right, key)
        if (t != None): return t.key
        else:           return x.key

def size(x):
        if (x == None): return 0
        return x.count

def rank(key, x):
        if (x == None): return 0
        if (key < x.key): return rank(key, x.left)
        elif (key > x.key): return 1 + size(x.left) + rank(key, x.right)
        else: return size(x.left)

def deleteMin(x):               # x should be the root
        if (x.left == None) return x.right
        x.left = deleteMin(x.left)
        x.count = 1 + size(x.left) + size(x.right)
        return x

def show_contents(x):
        if (x == None): return

        show_contents(x.left)
        print((x.key, x.val))
        show_contents(x.right)


root = Node(5, 'e')
insert(root, 6, 'f')
insert(root, 3, 'c')
insert(root, 7, 'g')
insert(root, 4, 'd')
insert(root, 10, 'j')
insert(root, 2, 'b')

a = get(root, 3)

show_contents(root)

print(size(root))
print(rank(3, root))




