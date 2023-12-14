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
    Implement Randomized partitioning from Cormen book
    20% Points will be deducted if you do not use RANDOMIZATION
    """
    pivot = randrange(low,high)
    temp_val = array[low]
    array[low] = array[pivot]
    array[pivot] = temp_val
    return Partition(array,low,high)



def QuickSort(array, low, high):
    """
    Implement Quicksort method using RandomizedPartition from Cormen book (Look at Section 7.3)
    40% points will be reduced if you do not use RandomizedPartition
    The array is sorted in place.
    """
    if low < high:
        q = RandomizedPartition(array,low,high)
        QuickSort(array,low,q-1)
        QuickSort(array,q+1,high)
    return array

def isAnagram(string1, string2):
    """
    Return true if string2 is an anagram of string1 otherwise return false
    Example of anagrams: (red, der) (abcdefg, bacdgfe)
    """
    string1_arr = []
    string2_arr = []
    for i in string1:
        string1_arr.append(i)
    for i in string2:
        string2_arr.append(i)
    QuickSort(string1_arr,0,len(string1_arr)-1)
    QuickSort(string2_arr,0,len(string2_arr)-1)
    if string1_arr == string2_arr:
        return True
    else:
        return False


def sortByOnesBits(array):
    """
    You are given an integer array.
    The goal is to sort the integers in ascending order by the number of 1's in their binary representation and
    when two or more integers have the same number of 1's, those numbers must be sorted in ascending order.
    Return the sorted array
    """

    #NOTE: This is probably super inefficient, but if it works it works.

    new_array = []
    #find max number of ones
    max_1s=0
    for i in array:
        if bin(i).count("1") > max_1s:
            max_1s = bin(i).count("1")
    print(max_1s)
    #sort by number of ones
    for i in range(0,max_1s+1):
        temp_array = []
        for j in range(len(array)):
            if bin(array[j]).count("1") == i:
                temp_array.append(array[j])
        QuickSort(temp_array,0,len(temp_array)-1)
        for k in temp_array:
            new_array.append(k)

    return new_array;
