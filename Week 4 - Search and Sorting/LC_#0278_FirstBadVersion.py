"""
https://leetcode.com/problems/first-bad-version/
"""

class Solution(object):
    def firstBadVersion(self, n):
        
        
        #method using the template 2 binary search
        l,r = 1,n
        
        while(l < r):
            mid = (l + r) //2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
                
        return l
        
        #n versions [1, 2, ..., n]
        #0 0 0 1 1
        
        
        
        #Vincent version original
        
        """
        #Start by initializing the two pointers
        left = 1
        right = n
        
        while left <= right:
            mid = (left + right)//2
            
            
                #First bad version is the n where:
                #isBadVersion(n-1) = False
                #isBadVersion(n) = True
                #isBadVersion(n+1) = True
            
        
            if isBadVersion(mid) == True:
                
                if isBadVersion(mid-1) == False:
                    return mid
                else:
                    right = mid
            else:
                #Need to add +1 to the left index
                #because we're trying to check what is the very first BAD version, not the last GOOD Version
                left = mid+1
                
        return 1
        """
