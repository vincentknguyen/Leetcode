#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:44:19 2021

@author: vincentnguyen
Time: O(n), due to the for loop iterating through an array "nums"
Space: O(n) 

https://leetcode.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self,nums):
        store = {}

        #iterating over a list, not its inices
        for i in nums:
            #store the number

            #if the numeb
            if i not in store:
                store[i] = 1
            else:
                del store[i]

        #turn it into a list to return the only item in the list
        return list(store.keys())[0]
        
