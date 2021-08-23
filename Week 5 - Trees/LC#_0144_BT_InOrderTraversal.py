"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        #In order traversal = left, root, right
        
        #1. Recursive result
        """
        res = []
        if root:
            res = self.inorderTraversal(root.left) 
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
        """
                
        #2. Iterative result
        
        stack = []
        result = []            
        
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
        
    
    
        
        

        
