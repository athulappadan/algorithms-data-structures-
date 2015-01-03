# simple quick find implementation

id_list = []

def list_init(N):
        for i in xrange(N):
                id_list.append(i)

def connected(p,q):
        return id_list[p] == id_list[q]

def union(p,q):
        pid = id_list[p]
        qid = id_list[q]
        for i in xrange(len(id_list)):
                if (id_list[i] == pid): id_list[i] = qid


list_init(10)

union(0,1)
a = connected(0,1)

print(a)
