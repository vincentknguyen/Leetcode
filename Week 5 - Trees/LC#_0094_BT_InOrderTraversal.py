"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
     1
    / \
   2    3
  / \  / \
 4  5  6  7

'''

class Solution(object):
    def inorderTraversal(self, root):
        #In order traversal = left, root, right
        
        #1. Recursive result
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 
        
        
        #res = []
        #if root:
        #    res = self.inorderTraversal(root.left) 
        #    res.append(root.val)
        #    res = res + self.inorderTraversal(root.right)
        #return res
        """

        stack = []
        result = []
        
        #Left root right
        
        while root is not None or stack != []:
            #you want to go all the way left first
            while root is not None:
                stack.append(root)
                root = root.left
                
            #stack = [1,]
            #result = [4,2,5]
            
            #You have now just traversed everything on the left
            #pop the current value in stack and append to result []
            root = stack.pop()
            result.append(root.val)
            
            #then check on the right
            root = root.right
        
        
        return result
        
    
    
        
        

        
        
    
    
        
        

        
