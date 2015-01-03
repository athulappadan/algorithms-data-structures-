id_list = []

def list_init(N):
        for i in xrange(N):
                id_list.append(i)

def root(i):
        while (i != id_list[i]): i = id_list[i]
        return i

def connected(p,q):
        return root(p) == root(q)

def union(p,q):
        i = root(p)
        j = root(q)
        id_list[i]= j



list_init(10)
union(3,4)
a = connected(3,4)
print(a)
