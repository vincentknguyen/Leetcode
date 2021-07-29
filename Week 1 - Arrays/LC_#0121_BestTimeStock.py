#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:36:05 2021

@author: vincentnguyen
Time: O(n) -> while loop
Space: O(n). Input of the function is an array, which takes up O(n) space


https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""

class Solution(object):
    def maxProfit(self,prices):
        #Initialize
        l = 0
        r = 1
        maxProfit = 0
        
        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
                
            else:
                l = r

            r += 1

        return maxProfit
