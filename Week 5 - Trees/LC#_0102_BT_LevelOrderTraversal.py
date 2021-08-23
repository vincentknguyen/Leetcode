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


[1]
[2,3]
[4,5,6,7]

'''

class Solution(object):
    def levelOrder(self, root):
        
        if root is None:
            return []
        
        queue = [root]
        next_queue = []
        level = []
        
        result = []
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                    
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
            
        return result
        
