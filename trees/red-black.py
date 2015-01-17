# Left leaning red-black tree implementation

RED = True
BLACK = False

class Node:
        def __init__(self, key, val, color):
                self.key = key
                self.val = val
                self.color = color
                self.left = None
                self.right = None

def get(x, key):
        while (x != None):
                cmp = compareKey(key, x.key)
                if (cmp < 0):   x = x.left
                elif (cmp > 0): x = x.right
                else:           return x.val

        return None

def leftRotate(h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

def rightRotate(h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

def flipcolors(h):
        assert (not isRed(h))
        assert isRed(h.left)
        assert isRed(h.right)

        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK

def put(h, key, val):
        if (h == None):
                return Node(key, val, RED)
        cmp = compareKey(key, h.key)
        if (cmp < 0):   h.left = put(h.left, key, val)
        elif (cmp > 0): h.right = put(h.right, key, val)
        else:           h.val = val

        if (isRed(h.right) and not isRed(h.left)):
                h = leftRotate(h)
        if (isRed(h.left) and isRed(h.left.left)):
                h = rightRotate(h)
        if (isRed(h.left) and isRed(h.right)):
                flipcolors(h)

        return h

def compareKey(key1, key2):
        if (key1 < key2):   return -1
        elif (key1 > key2): return 1
        else:               return 0

def isRed(h):
        if (h != None):
                return h.color == RED


root = Node('f', "friend", BLACK)

root = put(root, 'd', "dog")
root = put(root, 'g', "gate")
root = put(root, 'k', "kettle")
root = put(root, 'a', "apple")
root = put(root, 'r', "rabbit")
root = put(root, 's', "sea")

v = get(root, 'a')
print(v)
