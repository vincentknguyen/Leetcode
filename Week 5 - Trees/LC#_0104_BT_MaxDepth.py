'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #max depth of an empty tree is 0
        if not root:
            return 0
        
        #1a. Recursive Solution (DFS)
        #recursion is looking at the subproblem
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
                
            
        #1b. Recursive DFS
        '''
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        if l > r:
            return l + 1
        return r + 1
        '''
                    
            
            
        #2. Iterative BFS, basically level order traversal until you get to the last level
        #then count back

        
        #Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 
        #Deques support  thread-safe, memory efficient appends and pops from either side of the deque 
        #with approximately the same O(1) performance in either direction.
        
        '''
        #initialize
        level = 0                
        q = []
        q.append(root)
        
        
        #at each level you are trying to replace with the next
                
        while q:
            level += 1
            temp = []
            
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            q = temp
        return depth
        '''    
        
        #3. Iterative DFS
        
        stack = [[root,1]]
        res = 1
        while stack:
            node, depth = stack.pop()
        
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
                
        return res     
        
  
