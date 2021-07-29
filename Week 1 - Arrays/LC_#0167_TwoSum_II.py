#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:33:05 2021

@author: vincentnguyen
Time: O(n), while loop
Space: O(n), input is an array


https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution(object):
    def twoSum(self, numbers, target):
        #Initialize the 2 pointer positions (first and last)
        pointer1 = 0
        pointer2 = len(numbers) - 1

        
        #For loop
        while pointer1 < pointer2:    
            currentSum = numbers[pointer1] + numbers[pointer2]
            
            if currentSum > target:
                pointer2 = pointer2 - 1    

            elif currentSum < target:
                pointer1 = pointer1 + 1

            else:
                return [pointer1+1,pointer2+1]
