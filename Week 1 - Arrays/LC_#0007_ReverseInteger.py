#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:18:50 2021

@author: vincentnguyen

Time: O(n), due to the for loop going through the string
Space: O(1). Storing values in variables. So only storing 1 thing at a a time -> O(1)
    string = string + x_str[i]

https://leetcode.com/problems/reverse-integer/
"""

##Letcode - Reverse integer

class Solution(object):
    def reverse(self,x):       
        neg_limit =-0x80000000 # hex(-2**31-1),see details in accepted answer above
        pos_limit = 0x7fffffff

        string = ''    

        #check the first character and see if it's positive or negative(-1)

        x_str = str(x)
        if x_str[0] == "-":
            flag = -1
            x_str = x_str[1:]
        else:
            flag = 1
            x_str = x_str

        #go through the string, from back to front
        for i in range(len(x_str)-1,-1,-1):
            string = string + x_str[i]

        #return int(string)*flag
        temp = int(string)*flag


        #check if the constraints are met
        if (temp < neg_limit) or (temp > pos_limit):
            return 0
        else:
            return temp
