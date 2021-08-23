"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution(object):
    def searchRange(self, nums, target):
        #find the starting and ending position of a given target value.        
        #array of integers sorted in ascending order
        
        #so that means, once you find the target, you need to check if its the start or end
        #start: mid == target and (mid-1) != target
        #end: mid == target and  (mid + 1) = target
        
        #NEVER TRY TO SEARCH TWO THINGS AT ONCE
        if not nums:
            return [-1,-1]
        
        
        n = len(nums)
        left,right = 0,n        
        
        #Set the base cases
        start, end = -1,-1
        
        
        #Binary search #1 for Start
        while left < right:
            mid = (left + right)//2
            
            #we are always decreasing the right pointer until r is equal to l
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        #Check if l is out of bound
        if left < n and nums[left] == target:
            start = left
        
        #Binary search #2 for Start
        #re-initialize
        left,right = 0,n
        
        
        while left < right:
            mid = (left + right)//2
            
            #if start == end = [1,1]
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        if nums[right-1] == target:
            end = right - 1
        
        
        return [start,end]
        
        
        
        
        
