def quicksort(mylist):
        sort(mylist, 0, len(mylist) - 1)

def sort(a, low, hi):
        
        if hi <= low:
                return

        j = partition(a, low, hi)
        sort(a, low, j-1)
        sort(a, j+1, hi)


def partition(a, low, hi):

        i = low
        j = hi + 1

        while(1):
                
                i = i + 1
                while (a[i] < a[low]):
                        if (i == hi): break
                        i = i + 1

                j = j - 1
                while (a[low] < a[j]):
                        if (j == low): break
                        j = j - 1

                if (i >= j): break
                exch(a, i, j)

        exch(a, low, j)
        return j


def exch(a, i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

alist = [3,2,6,4]
quicksort(alist)
print(alist)

