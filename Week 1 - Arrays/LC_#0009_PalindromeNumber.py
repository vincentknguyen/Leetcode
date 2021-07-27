#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:25:47 2021

@author: vincentnguyen

Time: O(n), due to the while loop going through the array
Space: O(1). Memory used at once -> what is contained in the intermediate variables (temp, rev, dig)


https://leetcode.com/problems/palindrome-number/
"""

class Solution(object):
    def isPalindrome(self, x):
        neg_limit =-0x80000000 # hex(-2**31-1),see details in accepted answer above
        pos_limit = 0x7fffffff

        if (x < neg_limit) or (x > pos_limit):
            return False

        elif x < 0:
            return False

        else:

            #TRICK FOR REVERSING STRINGS/EXTRACTING DATA: doing the integer  mod 10        
            #% = remainder
            #// = floor

            temp = x
            rev = 0
            while(temp > 0):
                dig = temp % 10    #extract last digit by taking the remainder
                rev = rev * 10 + dig    #build up the reverse
                temp = temp//10       #Round down to nearest whole number

            #return rev

            if (rev == x):
                return True
            else:
                return False

    
    
    
    