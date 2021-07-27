#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:26:57 2021

@author: vincentnguyen

Time: O(n), due to the while loop going through the array
Space: O(1). Memory used at once is constant

https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""


s1 = "abcabcbb"


def longestSubstring(s):
    #Initialize variables for the sliding window
    result = 1
    left = 0
    right = 1

    #initialize a SET -> will contain only the unique values of the string
    seen = set(s[0])
    
    
    #moving the right pointer from index 1 -> end of string
    while right < len(s):
        
        #if there is a duplicate, shift window to the right by 1
        if s[right] == s[left]:
            left += 1
            right += 1
        
        #next char is found in the window
        # shift left edge of window to the right until next char is no longer in window

        elif s[right] in seen:
            while s[right] in seen:
                if s[left] in seen:
                    
                    #remove seen character from string
                    seen.remove(s[left])
                left += 1
            
            #expand right edge to include next char
            seen.add(s[right])
            right += 1
        
        #next char is new, expend the right edge
        else:
            seen.add(s[right])
            right += 1
        
        #Track the longest window
        if right - left > result:
            result = right - left
        
    return result
    
print(longestSubstring(s1))    
    