"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution(object):
    def search(self, nums, target):
        
    #Remember -> anytime you encounter a circular loop, think of using the modulo operator
    #1. Find the pivot point where it is left rotated
        n = len(nums)
        
        left,right = 0,n-1
        
        while (left < right):
            mid = (left + right)//2
            #if its greater, then pivot point must exist on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
                
            #if its lower, then pivot point must exist on the left side
            else:
                right = mid
                
        #Set the pivot
        pivot = left
        
        #2. Then do regular binary search using the pivot 
        left,right = 0,n-1
        
        while (left <= right):
            mid = (left+right)//2
            
            mid2 = (mid + pivot)%n
            if nums[mid2] ==target:
                return mid2
            
            elif nums[mid2] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1
    
    
    
    
