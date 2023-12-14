#!/usr/bin/python3

# Answer code for testing purposes. Allows you to make use of the test/ folder.
# Anything outside of the starter/ and test/ folder is optional.


def InsertionSort(array):
    """Sort the array of integers in increasing order using insertion sort

    Args:
        array: An array of integers.

    Note: You are not supposed to use python's inbuilt sorting function
    """
    for i in range(0,len(array)):

        insert_val = array[i]
        empty_val = i
        while(empty_val>0 and array[empty_val-1] > insert_val):
            print(array)
            array[empty_val] = array[empty_val-1]
            empty_val -= 1
        array[empty_val] = insert_val
    pass



def CountSwapsInInsertionSort(array):
    """Sort the array of integers (in increasing order) using insertion sort and count the total number of swaps required in the process
       see Figure 2.2 from the cormen book. Total number of swaps required for sorting the array 5,2,4,6,1,3 using insertion sort is 9 (total number of grey arrows)

    Args:
        array: An array of integers.
    """
    num_swaps = 0
    for i in range(0,len(array)):
        print(array)
        insert_val = array[i]
        empty_val = i
        while(empty_val>0 and array[empty_val-1] > insert_val):
            array[empty_val] = array[empty_val-1]
            empty_val -= 1
            num_swaps += 1
        array[empty_val] = insert_val
    return num_swaps



def countNumberOfInversions(array):
    """Count total number of inversions in array, an inversion is defined as a pair with elements a_i and a_j at position index position i and j with the condintion that a_i > a_j and i < j
    Example: total number of inversions in the array 110, 105, 95, 85, 0 is 10 corresponding to (110, 105), (110, 95), (110, 85), (110, 0), (105, 95), (105, 85), (105, 0), (95, 85), (95, 0) and (85, 0)

    Args:
        array: An array of integers.
    """
    num_inversion = 0
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if (i<j) and (array[i]>array[j]):
                num_inversion += 1
    return num_inversion
