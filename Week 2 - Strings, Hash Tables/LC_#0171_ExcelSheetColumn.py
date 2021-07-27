#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:29:55 2021

@author: vincentnguyen

Time: O(n), due to the for loop going through the string
Space: O(1). Memory used at once is constant

https://leetcode.com/problems/excel-sheet-column-number/
"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        #1 <= columnTitle.length <= 7
        #columnTitle is in the range ["A", "FXSHRXW"]
        #columnTitle consists only of uppercase English letters
        
        letter_dictionary = {
            'A': 1,
            'B': 2, 
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26                        
        }
        
        result = 0
        for i in range(len(columnTitle)):
            #Extract the value of the string
            #result = result*(26*i) + letter_dictionary[columnTitle[i]]
            result = result*26 + letter_dictionary[columnTitle[i]]

        return result
        
        
        
        