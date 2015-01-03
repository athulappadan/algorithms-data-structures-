#selection sort : O(N ^ 2)

def selectionSort(alist):
        for fillslot in range(len(alist) - 1, 0, -1):
                positionOfMax = 0
                for location in xrange(1, fillslot+1):
                        if alist[location] > alist[positionOfMax]:
                                positionOfMax = location

                temp = alist[fillslot]
                alist[fillslot] = alist[positionOfMax]
                alist[positionOfMax] = temp

alist = [12,56,34,11,78,88,99,52,7,1,34]
selectionSort(alist)
print(alist)

