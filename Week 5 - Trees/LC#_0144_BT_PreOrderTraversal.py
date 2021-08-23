"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        #Preorder = root, left, right
        
        #Base case: check when we need to exit the function
        if root is None:
            return []
        
        
        """
        #1. Recursive case: Root, left right
        #in list form, bcz we want to return it as a list
        
        #Concatenating numbers in empty lists = just the number
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        """
        
        
        #2. Iterative solution: using a stack (LIFO)
        stack = [root]
        result = []
        
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
                
            if root.left is not None:
                stack.append(root.left)
        
        return result
        
        
                
        
        
    
