pq = [0]

def swim(k):
        while (k > 1 and pq[k/2] < pq[k]):
                exch(k, k/2)
                k = k/2

def insert(x):
        pq.append(x)
        swim(pq.index(x))

def sink(k, N):
        while (2*k <= N):
                j = 2 * k
                if ((j < N) and pq[j] < pq[j+1]):
                        j = j + 1
                if (pq[j] < pq[k]):
                        break
                exch(k, j)
                k = j

def delMax():
        maxm = pq[1]
        exch(1, len(pq) - 1)
        sink(1)
        pq.pop()
        return maxm

def IsEmpty():
        return len(pq) == 1

def exch(i, j):
        temp = pq[i]
        pq[i] = pq[j]
        pq[j] = temp


def heapsort(pq):
        N = len(pq) - 1
        k = N/2
#        while (k >= 1):
#               sink(k, N)
#               k = k-1
        while (N > 1):
                exch(1, N)
                N = N - 1
                sink(1, N)



insert(10)
insert(16)
insert(19)
insert(23)
insert(7)
insert(8)
insert(15)

print pq

heapsort(pq)
print pq

