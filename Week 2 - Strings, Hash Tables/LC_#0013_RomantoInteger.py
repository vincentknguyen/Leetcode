"""
Time: O(n)
Space: O(1)

https://leetcode.com/problems/roman-to-integer/
"""


class Solution(object):
    def romanToInt(self, s):
        roman_dictionary = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
                
        #Output = the sum of the values            
        #Initialize with first character
        output = roman_dictionary[s[0]] 
        
        #case where length of string is 1
        if len(s) == 1:
            return output        
        else:
            
        #Iterate for the entire sting
            for i in range(1,len(s)):
                #Map the character
                temp = roman_dictionary[s[i]]

                if temp > roman_dictionary[s[i-1]]:
                    output = output - roman_dictionary[s[i-1]] + (temp - roman_dictionary[s[i-1]])
                    
                    #Example for MCMXCIV = 1994
                    #M = 1000
                    #C = 1100
                    #MCM = 1100 - 100 + 1000 - 100
                                        
                else:
                    #Take the sum of the output 
                    output = output + temp
            
            #Finally, return the output
            return output
