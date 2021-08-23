"""
https://leetcode.com/problems/find-peak-element/

"""


class Solution(object):
    def findPeakElement(self, nums):
        

        #if the array contains multiple peaks, return the index to any of the peaks.
        """
        [1,2,3,1] -> return 3
        """
        l,r = 0, len(nums)-1
        
        while(l < r):
            mid = (l + r) //2
            
            #check the condition
            #its a peak if the number after is lower
            
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
                
            else:
                r = mid
                
        return l    
        
