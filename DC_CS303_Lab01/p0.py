#!/usr/bin/python3

# Answer code for testing purposes. Allows you to make use of the test/ folder.
# Anything outside of the starter/ and test/ folder is optional.
import math

def binarySearch(array, target):
    """Apply binary search on array with the target number.

    Args:
        array: An array of integers in non-decreasing order.
        target: A int value which is target number.

    Return:
        Index of target number in array if find, otherwise, return -1.
    """

    #TODO: Implement without using python's in-built function
    print(target)
    if(type(array)==list):
        readd = 0
        for i in range(len(array)):
            half = len(array)//2
            if len(array) == 1:
                if array[half] == target:
                    return half+readd
                return -1
            if array[half] == target:
                return half
            elif array[half] > target:
                array = array[:half]
            elif array[half] < target:
                readd += half
                array = array[half:]
            if(len(array) <= 50):
                print(array)
            half = int(len(array)/2)
            if array[half] == target:
                return half+readd
            #bruh = input("Press key to continue...")
    return -1
    # return -2



def linearSearch(array, target):
    """Apply linear search on array with the target number.

    Args:
        array: An array of integers in non-decreasing order.
        target: A int value which is target number.

    Return:
        Index of target number in array if find, otherwise, return -1.
    """

    #TODO: Implement without using python's in-built function
    if(type(array)==list):
        for i in range(0, len(array)):
            if(array[i] == target):
                return i
    return -1
    # return -2
