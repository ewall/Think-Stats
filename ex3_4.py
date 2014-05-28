# Example 3-4

def selectsort(lst):
    # selection sort, for reference
    for i in range(0, len(lst)-1):
        mn = min( range(i,len(lst)), key=lst.__getitem__ )
        lst[i],lst[mn] = lst[mn],lst[i]
    return lst

def select(lst, k):
    # selection sort up to kth element
    for i in range(0, k):
        mn = min( range(i,len(lst)), key=lst.__getitem__ )
        lst[i],lst[mn] = lst[mn],lst[i]
    return lst[k]

def quicksort(lst, l, r):
    # quicksort, for reference
    # from Sedgewick "Algorithms in C++" p118
    # to sort entire list: quicksort(list,0,len(list)-1)
    if (r > l):
        v, i, j = lst[r], l, r-1
        while True:
            while lst[i] < v:
                i += 1
            while lst[j] > v:
                j -= 1
            if i >= j:
                break
            lst[i], lst[j] = lst[j], lst[i]
        lst[i], lst[r] = lst[r], lst[i]
        quicksort(lst, l, i-1)
        quicksort(lst, i+1, r)

def quickselect(lst, n, k):
    # select kth element using quicksort-style partitioning
    # from Sedgewick "Algorithms in C++" p128
    pass
    
def main():
    scores = [99, 66, 55, 88, 77]
    rank = 80
    index = rank * (len(scores)-1) / 100
    print "If you percentile rank was {0}:".format(rank)
    print "...selectsort says your score must be {0}".format(select(scores, index))
    #print "...quickselect says your score must be {0}".format(quickselect(scores, index))

if __name__ == '__main__':
    main()