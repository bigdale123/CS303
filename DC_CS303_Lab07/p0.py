#!/usr/bin/python3


class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None



def insert(root, key, value):
    """
    Insert a new Node to the Binary Search Tree.

    Args:
        root: The root of Tree
        key: A integer, the key of node
        value: A String, the value of node

    Return:
        (optional) The root of tree so that we can create a tree with
    """
    newnode = TreeNode(key, value)

    y = None
    while (root is not None):
        y=root
        if key < root.key:
            root = root.left
        elif key > root.key:
            root = root.right
    if (y == None):
        y = newnode
    elif (key < y.key):
        y.left = newnode
    else:
        y.right = newnode
    return root




def search(root, key):
    """
    Search the key in BST.

    Args:
        root: The root of BST
        key: A integer, the key of node

    Return:
        If exits, return the value of node.
        Otherwise, return None.
    """
    while root and key != root.key:
        if key < root.key:
            root = root.left
        else:
            root = root.right
    if root == None:
        return root
    else:
        return root.value
    # if root is None or root.value != key:
    #     return root.value
    # if root.value < key:
    #     return search(root.right,key)
    # else:
    #     return search(root.left,key)



def inorder_traversal(root):
    """
    Traverse the BST with In-order traversal method.

    Args:
        root: The root of BST
        
    Return:
        returns a list of keys from the BST traversed in-order.
    """
    list = []
    if root == None:
        return list
    list.extend(inorder_traversal(root.left))
    list.extend([root.key])
    list.extend(inorder_traversal(root.right))
    return list



def buildBST(tuples):
    """
    Use the data that read from file to build a binary search tree.

    Args:
        tuples: tuples is a list of tuple, which are made of key value pairs
        Example of tuples: [(9800910632,"ct"),(4700007710,"LB"),(8811323523,"The"),(9400000351,"oz")]
    Return:
        Return the root of the tree.
    
    """
    if len(tuples) != 0: 
        root = TreeNode(tuples[0][0],tuples[0][1])
        for i in range(1,len(tuples)):
            insert(root, tuples[i][0], tuples[i][1])
        return root
