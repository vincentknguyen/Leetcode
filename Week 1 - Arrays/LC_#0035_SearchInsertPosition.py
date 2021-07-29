#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:36:32 2021

@author: vincentnguyen

Time: O(logn), due to the 2 pointers approach dividing the response in half (binary search)
Space: O(1). Memory used at once -> the 3 value of middle, left and right. Therefore, space complexity scales constantly depending on input


https://leetcode.com/problems/search-insert-position/
"""

class Solution(object):
    def searchInsert(self, nums, target):

        #Initialize the pointer indices
        left = 0
        right = len(nums)-1

        #for Olog(n) searching, use Binary search on an array
        while left <= right:
            middle = (left + right)//2

            if nums[middle] == target:
                return middle
            elif(nums[middle] < target):
                left += 1
            else:
                right -= 1

        return left
    
    
    
    
