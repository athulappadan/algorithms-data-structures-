# AVL tree implementation

class Node:
        def __init__(self, key, val):
                self.key = key
                self.val = val
                self.heightFactor = 1
                self.left = None
                self.right = None

def height(node):
        if (node == None):
                return 0
        return node.heightFactor

def getBalance(node):
        if (node == None):
                return 0
        return height(node.left) - height(node.right)
                

def rotateLeft(h):
        x = h.right
        h.right = x.left
        x.left = h

        h.heightFactor = max(height(h.left) + height(h.right)) + 1
        x.heightFactor = max(height(x.left) + height(x.right)) + 1

        return x

def rotateRight(h):
        x = h.left
        h.left = x.right
        x.right = h

        h.heightFactor = max(height(h.left) + height(h.right)) + 1
        x.heightFactor = max(height(x.left) + height(x.right)) + 1

        return x

def insert(h, key, val):
        if (h == None): return Node(key, val)

        if (key < h.key):
                h.left = insert(h.left, key, val)
        elif (key > h.key):
                h.right = insert(h.right, key, val)
        else:
                h.val = val

        balance = getBalance(h)

        if (balance > 1 and (key < h.left.key)):            # left left case
                return rotateRight(h)

        if (balance > 1 and (key > h.left.key)):            # left right case
                h.left = rotateLeft(h.left)
                return rotateRight(h)

        if (balance < -1 and (key < h.right.key)):          # right left case
                h.right = rotateRight(h.right)
                return rotateLeft(h)

        if (balance < -1 and (key > h.right.key)):          # right right case
                return rotateLeft(h)

        return h

def getVal(x, key):
        while (x != None):
                if (key < x.key):
                        x = x.left
                elif (key > x.key):
                        x = x.right
                else:
                        return x.val

        return None

root = None
root = insert(root, 'f', "friend")
root = insert(root, 'h', "hat")
root = insert(root, 'c', "cricket")

print(getVal(root, 'c'))
