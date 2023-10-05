#Implementation of binary searh algorithm

#We will prove that binary search is faster than naive search

#naive search: scan entire list and asks if it is equal to the target
#if yes, return the index
# if no, then return -1
def naive_search(l, target):
    for i in range(len(l)):
        if l(i) == target:
            return i 
    return -1



# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    
    # example l = [1, 3, 5, 10, 12]  # should return 3
    midpoint = (low + high) // 2 #2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
    
    if __name__ == '__main__':
        l = [1,3,5,10,12]
        target = 10
        print(naive_search(l, target))
        print(binary_search(1,target))