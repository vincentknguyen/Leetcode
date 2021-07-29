#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:43:53 2021

@author: vincentnguyen
Time: O(n + n) done by the two (non-nested) for loops
Space: O(n). Integer array as an input

https://leetcode.com/problems/move-zeroes/

"""

class Solution(object):
    def moveZeroes(self,nums):
        index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[index]  = nums[i]
                #this will define how many zeroes you need to have
                index += 1


        for j in range(index,len(nums)):
            nums[j] = 0
