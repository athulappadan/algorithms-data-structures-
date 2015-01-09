pq = [-1]

def N():
        return len(pq) - 1

def isEmpty():
        return N() == 0

def swim(k):
        while (k > 1 and more(k/2, k)):
                exch(k, k/2)
                k = k/2

def insert(x):
        pq.append(x)
        swim(N())

def sink(k):
        while (2*k <= N()):
                j = 2*k
                if (j < N() and (j+1) < N() and more(j, j+1)):
                                j += 1
                if (not more(k, j)): break
                exch(k, j)
                k = j

def delMin():
        min = pq[1]
        exch(1, N())
        pq.pop()
        sink(1)

        return min

def more(i, j):
        return pq[i] > pq[j]

def exch(i, j):
        temp = pq[i]
        pq[i] = pq[j]
        pq[j] = temp

insert('v')
insert('p')
insert('a')
insert('y')
insert('m')
insert('d')
insert('q')
insert('z')
insert('o')
insert('l')
insert('u')
insert('b')
insert('f')
insert('r')
insert('h')
