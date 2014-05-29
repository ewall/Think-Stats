# Example 3-4

import random

def selectsort(lst):
    """selection sort, for reference"""
    for i in range(0, len(lst)-1):
        mn = min( range(i,len(lst)), key=lst.__getitem__ )
        lst[i],lst[mn] = lst[mn],lst[i]
    return lst

def select(lst, k):
    """selection sort up to kth element"""
    for i in range(0, k):
        mn = min( range(i,len(lst)), key=lst.__getitem__ )
        lst[i],lst[mn] = lst[mn],lst[i]
    return lst[k]

def listselect(lst, k):
    """pythonic use of list comprehensions"""
    return [x for x in lst if len( [y for y in lst if y < x]) == k][0]

def quicksort1(lst, l, r):
    """quicksort from Sedgewick "Algorithms in C++", p118"""
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
        quicksort1(lst, l, i-1)
        quicksort1(lst, i+1, r)

def quickselect1(lst, k):
    """select kth element using quicksort-style partitioning"""
    # from Sedgewick "Algorithms in C++", p128
    l, r = 0, len(lst)-1
    while (r > l):
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
        if i >= k:
            r = i-1
        if i <= k:
            l = i+1
    return lst[k]
 
def quicksort2(lst):
    """quicksort using list comprehensions"""
    # from http://en.literateprograms.org/Quicksort_%28Python%29
    # optional: flatten final results with compiler.ast.flatten() in Python 2
    if lst == []:
        return []
    pivot = lst[0]
    left = [x for x in lst[1:] if x < pivot]
    right = [x for x in lst[1:] if x >= pivot]
    #print
    #print "lst = ", lst
    #print "pivot = ", pivot
    #print "left = ", left
    #print "right = ", right
    return [quicksort2(left), pivot, quicksort2(right)]

def quickselect2(lst, k):
    """my quickselect using list comprehensions"""
    while True:
        pivot = random.choice(lst)
        #print "lst:", lst, "k:", k, "pivot:", pivot
        left = [x for x in lst if x < pivot]
        right = [x for x in lst if x >= pivot]
        if k < len(left):
            lst = left
        elif k == len(left):
            return pivot
        else:
            lst = right
            k -= len(left)

def main():
    scores = [99, 66, 55, 88, 77]
    rank = 80
    index = rank * (len(scores)-1) / 100
    print "If you percentile rank was {0}:".format(rank)
    for method in [select, listselect, quickselect1, quickselect2]:
        scores = [99, 66, 55, 88, 77]
        print "- {0} finds score {1}".format(method.__name__, method(scores, index))

if __name__ == '__main__':
    main()