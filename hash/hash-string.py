# simple hash function using horner's method

def hashVal(str):
        h = 0
        for i in xrange(len(str)):
                h = ord(s[i]) + (31 * h)
        return h

s = "athul"
print(hashVal(s))
print(hashVal("call"))

