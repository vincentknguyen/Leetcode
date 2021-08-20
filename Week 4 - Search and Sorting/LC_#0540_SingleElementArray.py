"""

https://leetcode.com/problems/single-element-in-a-sorted-array/

"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        
        #Every element appears exactly twice, except for one
        #O(log n) time
        #O(1) space
        """
        NON log n solution
        return 2*sum(set(nums)) - sum(nums)
        """
        #0 1 2 3 4
        #1 3 3 5 5 
        
        
        #0 1 2 3 4 5 6 
        #1 3 3 5 5 7 7
        
        
        #O log(n) solution        
        #index = [0,....n-1]
        n = len(nums)
                
        low=0
        high=n-1
        
        if high == 1:
            return nums[high]
        
        
        while low<high:
            mid=(low+high)//2
            
            if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                low=mid+1
            else:
                high=mid
        return nums[low]
