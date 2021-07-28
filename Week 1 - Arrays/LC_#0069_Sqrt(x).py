#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:29:02 2021

@author: vincentnguyen

Time: O(n), due to the while loop 
Space: O(n)
https://leetcode.com/problems/sqrtx/
"""

class Solution(object):
    
    def mySqrt(self,x):
            
        if (x <= 0) or (x > 2**31 - 1):
            return 0

        if x == 1:
            return 1

        temp = 1
        temp_squared = 1
        while temp_squared < x:
            temp_squared = temp*temp
            if temp_squared >= x:

                if temp_squared == x:                
                    return temp
                else:
                    return temp - 1

            else:
                temp = temp + 1
        
"""
    #More optimal solution
        Time: O(log n), due to Binary search
        Space: O(1)
        
        
    def mySqrt(self, n):
            if n == 0:
                return 0
            
            if n == 1:
                return 1
            
            start = 1
            end = n
            
            while start <= end:
                mid = (start+end)//2

                if mid*mid == n:
                    return mid

                if mid*mid < n:
                    start = mid + 1
                    ans = mid
                else:
                    end = mid - 1
            return ans
"""
