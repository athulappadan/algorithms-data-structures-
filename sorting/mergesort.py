def mergesort(mylist):
        aux = []
        for k in xrange(0, len(mylist)):
                aux.append(0)
        sort(mylist, aux, 0, len(mylist) - 1)

def sort(a, aux, lo, hi):
        if (hi <= lo): return

        mid = lo + (hi - lo) / 2
        sort(a, aux, lo, mid)
        sort(a, aux, mid+1, hi)
        merge(a, aux, lo, mid, hi)


def merge(a, aux, low, mid, hi):

        for k in xrange(low, hi+1):
                aux[k] = a[k]

        i, j = low, mid + 1

        for k in xrange(low, hi+1):

                if i > mid:
                        a[k] = aux[j]
                        j += 1

                elif j > hi:
                        a[k] = aux[i]
                        i += 1

                elif aux[j] < aux[i]:
                        a[k] = aux[j]
                        j += 1

                else:
                        a[k] = aux[i]
                        i += 1

alist = [4,3,2,1]
mergesort(alist)
print(alist)


