#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:30:35 2021

@author: vincentnguyen

Time: O(n), due to the for loop going through the array (i to len(arr))
Space: O(n). The amount of memory used at once increases linearly, as the size of the input increases

https://leetcode.com/problems/two-sum/

"""


class Solution(object):
    def twoSum(self,nums, target):
        #store the complements in a hashmap/dictionary
        #map of the complement of the number to its index
        complementMap = dict()
        ## <7,0>

        #O(n) due to the for loop
        for i in range(len(nums)):

            #start populating the complement map, in order
            num = nums[i] #0

            #Storing the complement of a specific number
            complement = target - nums[i] #complement = 7

            #if the number is in the dictionary, return its position in the dictionary
            if num in complementMap:
                return [complementMap[num], i] #complement
            else:

                #if not, store it within the 
                complementMap[complement] = i   #{7,0} = #key, value
                
                
