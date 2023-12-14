#!/usr/bin/python3


class TreeNode:
    """
    The basis of the BST.
    key: An integer, what we use to check equality with other nodes
    value: A string, the value returned from the node
    size: An integer, the size of the subtree beneath the node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.size = 0
        self.left = None
        self.right = None


def insert(root, key, value):
    """
    Insert a new Node to the Binary Search Tree.

    Args:
        root: The root of Tree
        key: An integer, the key of node
        value: A String, the value of node

    Return:
        (optional) The root of tree so that we can create a tree with
    """
    if not root:
        return TreeNode(key=key, value=value)
    if root.key == key:
        return root
    elif root.key < key:
        root.size += 1
        root.right = insert(root.right, key, value)
    else:
        root.size += 1
        root.left = insert(root.left, key, value)
    return root


def buildBST(tuples):
    """
    Use the data that read from file to build a binary search tree.

    Args:
        tuples: tuples is a list of tuple, which are made of key value pairs
        Example of tuples: [(9800910632,"ct"),(4700007710,"LB"),(8811323523,"The"),(9400000351,"oz")]
    Return:
        Return the root of the tree.
    
    """
    if not tuples:
        return
    root = TreeNode(tuples[0][0], tuples[0][1])
    for i in range(1, len(tuples)):
        insert(root, tuples[i][0], tuples[i][1])
    return root


def ithOrderStatistic(root, i):
    """
    Return the ith order statistic from the given BST using the logarithmic method
    where nodes are augmented with the size of their subtree.

    Args:
        root: The root of BST
        i: An integer, the order statistic to look for
    Return:
        Return the value of the ith order node
    """
    if root is None:
        return None
    if root.left is None:
        a=0 
    else:
        a=root.left.size
    if a >= i:
        return ithOrderStatistic(root.left, i)
    elif a < i-1:
        return ithOrderStatistic(root.right, i-a-1)
    else:
        return root.value


def maxHeight(root):
    """
    Return the max height (length from root to furthest leaf) of the given BST.

    Args:
        root: The root of BST
    Return:
        Return the integer maximum height of the BST
    """
    if root == None:
        return 0
    else:
        return 1 + max(maxHeight(root.left), maxHeight(root.right))


def getLeaves(root):  
    """
    Return all of the leaves (nodes with no right or left subtrees) of a given BST.

    Args:
        root: The root of BST
    Return:
        Return a sorted list of all the values of the leaf nodes of the BST.
    """
    s1 = []
    s2 = []
    s3 = []
    s1.append(root)
    while len(s1) != 0:
        curr = s1.pop()
        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)
        elif not curr.left and not curr.right:
            s2.append(curr)
    
    for i in s2:
        s3.append(i.value)
    return sorted(s3)


def majorityElement(arr):
    """
    Given an array arr, find and return the majority element (element that appears more than n/2 times). 

    Args: 
        arr: A list of integers with a guaranteed majority element
    Return:
        Return the majority element. 
        
    """
    # dict=()
    # dict={value:count}
    # for key, value in dict:
    #     if value > len(arr)/2:
    #         return key
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count+=1
        if count > len(arr)/2:
            return i
    return -1


def threeDuplicates(arr):
    """
    Given an array arr, it is gauranteed that all of the elements of the array will appear atleast three times except for one; Find and return this one element.
    if arr = [2,3,4,5,6,2,4,5,6,3,5,6,2,3,2,2,3,3,4,5,6,6,7,1,1,1] return 7
    if arr = [1,2,3,1,2,3,1,2,3,5,5] return 5
       
    Args:
        arr: A list of integers where every element appears atleast three times except for one.
    Return:
        Return the element that only appears once.
    """
    if len(arr) < 3:
        return -1
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count+=1
        if count == 1 or count == 2:
            return i
    return -1
