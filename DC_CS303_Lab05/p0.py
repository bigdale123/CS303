#!/usr/bin/python3
from random import randrange

def Partition(array,low,high):
    x = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= x:
            i += 1
            temp_val = array[i]
            array[i] = array[j]
            array[j] = temp_val
    temp_val = array[i+1]
    array[i+1] = array[high]
    array[high] = temp_val
    return i+1

def RandomizedPartition(array, low, high):
    """
    Implement Randomized partitioning from Cormen book (same as lab 4)
    """
    pivot = randrange(low,high)
    temp_val = array[low]
    array[low] = array[pivot]
    array[pivot] = temp_val
    return Partition(array,low,high)

def OrderStatistics_Helper(array,p,r,i):
    if p == r:
        return array[p]
    q = RandomizedPartition(array,p,r)
    k = q - p + 1
    #print("p = "+str(p)+", r = "+str(r)+", q = "+str(q)+", k = "+str(k))
    if i == k:
        #print("pog")
        return array[q]
    elif i < k:
        #print("poggers")
        if r == 1:
            return array[p]
        else:
            return OrderStatistics_Helper(array,p,q-1,i)
    else:
        #print("pogchamp")
        return OrderStatistics_Helper(array,q+1,r,i-k)

def OrderStatistics(array, p, r, i):
    """
    Return ith order statistics
    OrderStatistics(array, p, r, i), returns  the ith smallest element of the array array[p...r]

    For example in array = [81,71,99,68,45,55,0,22,11,34]
    return 0 for i = 0 [smallest]
    return 11 for i = 1
    return 22 for i = 2
    return 34 for i = 3
    return 45 for i = 4
    return 55 for i = 5
    return 68 for i = 6
    return 71 for i = 7
    return 81 for i = 8
    return 99 for i = 9 [largest]

    Your solution should run in lineartime using RandomizedPartition.
    40% points will be deducted for non-linear solutions

    For hints check Chapter 9 from Cormen book.

    """
    #Super Hack! needed to increment i by one before recursively calling function
    i += 1
    return OrderStatistics_Helper(array,p,r,i)


print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,0))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,1))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,2))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,3))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,4))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,5))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,6))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,7))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,8))
print(OrderStatistics([81,71,99,68,45,55,0,22,11,34],0,9,9))
