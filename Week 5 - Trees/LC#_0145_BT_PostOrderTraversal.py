"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        #Post order = left, right, root
        
        #1. Recursive result
        """
        res = []
        if root:
            res = self.postorderTraversal(root.left) 
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)
            
        return res
        """
        
        #2. Iterative solution
        
        result=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root) # push nodes into the stack
                root=root.left if root.left else root.right
            root=stack.pop()
            result.append(root.val) #Deal with the root node whenever it is popped from stack
            if stack and stack[len(stack)-1].left==root: #check whether it has been traversed 
                root=stack[len(stack)-1].right
            else:
                root=None #Force to quit the loop
        return(result)
        
        
