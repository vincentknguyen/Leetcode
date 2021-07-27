#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:33:36 2021

@author: vincentnguyen

Time: O(n*2) = O(n), due to the for and while loops going through the string s
Space: O(1). Memory used at once is what gets stored in the Complement Hashmap. Using a hashmap is O(1)

"""

#O(n) runtime
#O(1) space

class Solution(object):
    def firstUniqChar(self, s):
        
        count = {}
        
        #Step 1: Count the occurrences of each char in the string
        for char in s:
            
            #If character is in the dictionary, increment the count
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        
        #Step 2: Find the first unique character
        #initialize an index variable
        i = 0
        
        #use a while loop to go through the string
        
        while i < len(s):
            #check if count at index of character is equal to 1
            #this is bcz you are trying to find the FIRST String
            if count[s[i]] == 1:
                #return the character
                return i
            
            #increment 
            i += 1
        
        return -1
    
        
    
        