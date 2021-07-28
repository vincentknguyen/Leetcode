#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:34:49 2021

@author: vincentnguyen

Time: O(n) done by the for loop (going through all n units of input). For each item, do a lookup
    O(n + c * n) = O(n)
    
Space: O(n). At the limit, your map will have every single element in the original input

https://leetcode.com/problems/contains-duplicate/
"""

class Solution(object):
    def containsDuplicate(self,nums):
        duplicateMap = dict()
        for i in range(0,len(nums)):
                #start populating the complement map, in order
            num = nums[i]

                #if the number is in the dictionary, return its position in the dictionary
            if num in duplicateMap:
                return True
            else:

                    #if not, store it within the dictionary
                duplicateMap[nums[i]] = 2
                #duplicateMap[i] = num   

        return False
    
    
    """
    #Brute Force Solution
    def containsDuplicate(self,nums):
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    
    #HashMap solution
    def containsDuplicateMAP(self,nums):
        
        duplicateMap = dict()
        for i in range(0,len(nums)):
            #start populating the complement map, in order
            num = nums[i]
        
            #if the number is in the dictionary, return its position in the dictionary
            if num in duplicateMap:
                return True
            else:

                #if not, store it within the dictionary
                duplicateMap[i] = num   
                
        return False
    """
 
