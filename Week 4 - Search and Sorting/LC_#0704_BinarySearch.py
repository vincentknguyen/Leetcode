"""
https://leetcode.com/problems/binary-search/

"""

class Solution(object):
    def search(self, nums, target):
        #Sorted in ascending order
        
        #Ex: nums = [-1,0,3,5,9,12]
        #O log n runtime complexity
        
        n = len(nums)
        
        #Initialize left and right pointers
        l,r = 0, n-1
        
        while l <= r:
            mid = (l+r)//2
                        
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        #If you exit the loop, means you could not find the result
        #therefore, return -1
        return -1
