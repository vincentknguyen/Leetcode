"""
https://leetcode.com/problems/first-bad-version/
"""

class Solution(object):
    def firstBadVersion(self, n):
        #All the versions after a bad version are also bad
        
        #Start by initializing the two pointers
        left = 1
        right = n
        
        #n versions [1, 2, ..., n]
        #0 0 0 1 1
        
        #Time limit exceeded
        while left <= right:
            mid = (left + right)//2
            
            """
            First bad version is the n where:
                isBadVersion(n-1) = False
                isBadVersion(n) = True
                isBadVersion(n+1) = True
            """
        
            if isBadVersion(mid) == True:
                
                if isBadVersion(mid-1) == False:
                    return mid
                else:
                    right = mid
            else:
                #Need to add +1 to the left index
                #because we're trying to check what is the very first BAD version, not the last GOOD Version
                left = mid+1
