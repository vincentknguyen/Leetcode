#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:37:17 2021

@author: vincentnguyen

Time: O(n), for loop 
Space: O(n). Input is an array

https://leetcode.com/problems/majority-element/
"""

class Solution(object):
    def majorityElement(self,nums):
        majority = len(nums)/2
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

            if hashmap[i] > majority:
                return i
            
            
            
    """
    def majorityElement(self, nums):
        majority = nums[0]
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
                
                if(count == 0):
                    majority = nums[i]
                    count = 1
                
        return majority
    """    
        
        
