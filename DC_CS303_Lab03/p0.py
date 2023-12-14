#!/usr/bin/python3


def Merge(L, R, arr):
    """Merge function takes in as input two sorted lists "L" and "R", and a list "arr" of length len(L) + len(R) and merges the two sorted lists into the sorted list "arr"

    Args:
        L: sorted list
        R: sorted list
        arr: list of length len(L) + len(R)

    Note: You are not supposed to use python's inbuilt sorting function
    Note: Merge the sorted list L, and R into a sorted list "arr" in linear running time

    """
    i,j,k=0,0,0
    while(i<len(L) and j<len(R)):
        #print(arr)
        if L[i] <= R[j]:
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1
    while(i<len(L)):
        #print(arr)
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<len(R)):
        #print(arr)
        arr[k]=R[j]
        j+=1
        k+=1


def inversionCount_Merge(L, R, arr):
    """inversionCount_Merge function takes in as input two sorted lists "L" and "R", and a list "arr" of length len(L) + len(R) and merges the two sorted lists into the sorted list "arr" and returns the total number of split inversions between L and R

    Args:
        L: sorted list
        R: sorted list
        arr: list of length len(L) + len(R)

    Note: You are not supposed to use python's inbuilt sorting function
    Note: Merge the sorted list L, and R into a sorted list "arr" and returns the total number of split inversions in linear running time

    """
    inversions=0
    i,j,k=0,0,0
    while(i<len(L) and j<len(R)):
        if L[i] <= R[j]:
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1
            inversions+=len(L)-i
    while(i<len(L)):
        arr[k]=L[i]
        i+=1
        k+=1
    while(j<len(R)):
        arr[k]=R[j]
        j+=1
        k+=1

    return inversions

def MergeSort(array):
    """Sort the array of integers using Mergesort sort

    Args:
        array: A list of integers.

    Note: You are not supposed to use python's inbuilt sorting function
    Note: You are supposed to implement the function Merge first ans use the function Merge to implement MergeSort.
          Merge function takes in as input two sorted lists "L" and "R", and a list "arr" of length len(L) + len(R) and merges the two sorted lists into the sorted list "arr"
    """
    if(len(array)!=0):
        midpoint = len(array)//2
        print("MIdpoint: "+str(midpoint))
        L = array[:midpoint]
        R = array[midpoint:]
        print("L = "+str(L))
        print("R = "+str(R))
        if len(array)!=1 and len(array)!=2:
            MergeSort(L)
            MergeSort(R)
        Merge(L,R,array)



def inversionCount_MergeSort(array):
    """Count total number of inversions in array, an inversion is defined as a pair with elements a_i and a_j at position index position i and j with the condintion that a_i > a_j and i < j
    Example: total number of inversions in the array 110, 105, 95, 85, 0 is 10 corresponding to (110, 105), (110, 95), (110, 85), (110, 0), (105, 95), (105, 85), (105, 0), (95, 85), (95, 0) and (85, 0)

    Args:
        array: An array of integers.

    NOTE:
    	You are supposed to use the divide and conquer approach to count total number of inversions, as taught in the class
    	You have to implement the inversionCount_Merge first before you implement this.

    	inversionCount_Merge takes in as input two sorted lists, L and R and an list arr of length = len(L) + len(R)
    	The function returns the total number of split inversions between the lists L and R, and merges the two sorted list L and R into the sorted list arr
    """
    inv_count = 0
    if(len(array)!=0):
        midpoint = len(array)//2
        #print("MIdpoint: "+str(midpoint))
        L = array[:midpoint]
        R = array[midpoint:]
        #print("L = "+str(L))
        #print("R = "+str(R))
        if len(array)!=1 and len(array)!=2:
            inv_count += inversionCount_MergeSort(L)
            inv_count += inversionCount_MergeSort(R)
        inv_count += inversionCount_Merge(L,R,array)
        return inv_count
    else:
        return 0

#MergeSort([1,2,3,4,5,6,7,8,9])
