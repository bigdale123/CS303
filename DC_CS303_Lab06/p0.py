#!/usr/bin/python3
import math

def deduplicate(array):
    """
    return the total number of unique elements in array
    for example for
    array = [1,10,2,3,4,5,1,1,1,1,2], return 6
    array = [5,5,5,5], return 1
    array = [1,1,1,1,1,2,2,2,3,3,3,3], return 3
    """
    unique = []
    for i in array:
        if i not in unique:
            unique.append(i);

    return len(unique)



def twoSum(array, target):
    """
    Given an array of integers array and an integer target, return indices of the two numbers such that they add up to target, and also return the two numbers.
    the returned indices should be in increasing order.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    For example,
    array = [2,7,11,15], target = 9
    return (0, 1, 2, 7) as array[0] + array[1] == 9
    """
    tab=dict()
    for i in range(len(array)):
        a = target-array[i]
        if a in tab:
            return(tab[a],i,a,array[i])
        else:
            tab[array[i]]=i

def computeFibonacci(n):
    """
    Return the nth Fibonacci number
    Fibonacci Series: 0,1,1,2,3,5,8,13.......
    0th Fibonacci number is 0
    1st Fibonacci number is 1
    2nd Fibonacci number is 1
    and so on
    """
    i = 1
    j = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for k in range(1, n):
        i, j = j, i + j
    return j


def climbStairs(n):
    """
    There are n steps to reach the top of a building.
    Each time you can either climb 1 or 2 steps.
    Return the total number of distinct ways can you climb to the top?

    For example:
    when n = 1 return 1 (1 step)
    when n = 2 return 2 (1 step + 1 step OR 2 step)
    when n = 3 return 3 (1 step + 1 step + 1 step OR 2 step + 1 step OR 1 step + 2 step)

    """
    #print(n)
    q=0
    w=1
    e=2
    if n > 0:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for i in range(2,n):
                q=w+e
                w=e
                e=q
            return q
    else:
        return 0
