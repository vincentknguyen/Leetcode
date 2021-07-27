#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:36:05 2021

@author: vincentnguyen
Time: O(logn), due to the 2 pointers approach dividing the response in half (binary search)
Space: O(1). Memory used at once -> what is contained in the intermediate variables 


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