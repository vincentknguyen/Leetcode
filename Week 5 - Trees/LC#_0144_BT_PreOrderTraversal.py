"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
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

#Recursive solution -> THINK OF IT AS A CALL TRACE
[1] + 2 + 3
[2] + 4 + 5
[3] + 6 + 7

'''

'''
#Stack solution
stack = [3,2]
result = [1]


stack = [3,5,4]
result = [1,2]


stack = [3,5]
result = [1,2,4,5]
'''

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
        
        #2. Iterative solution: using a stack (LIFO), instead of a call stack
        stack = [root]
        result = []
        
        
        #whilt stack is not empty
        while stack != []:
             
            #pop -> removes and returns last value from ist
            root = stack.pop()
            result.append(root.val)
            
            #if a right child exists, add it first to the stack
            if root.right is not None:
                stack.append(root.right)
            
            
            #if a left child exists, add it second to the stack            
            if root.left is not None:
                stack.append(root.left)
        
        return result
        
      
                
        
        
    
