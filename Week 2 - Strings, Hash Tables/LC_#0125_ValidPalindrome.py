"""

https://leetcode.com/problems/longest-palindrome/

2 pointer solution:
  Time: O(log n) -> left and right pointers, dividing the problem in half
  Space: O(n) -> String as an input
  

Brute force solution:
  Time: O(n + log n) = O(n). Searching through the string once to remove all characters, then searching through it again with two pointers
  Space: O(n) -> String as an input
  
"""



class Solution(object):
    def isPalindrome(self, s):
    
        left = 0
        right = len(s)-1
        
        while left < right:
            
            #increment the left and right pointers if you hit a character that ISNT alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1
            
            #at any time that the left and right pointers arent equal
            #return False
            if s[left].lower() != s[right].lower():
                return False
            
            #increment both pointers after each comparison
            left += 1
            right -= 1
        
        #If everything is right, return True
        return True
        
    
    #Brute force solution -> traversing the string twice: 1 to clean it, 1 to do the palindrome check
    """
        s3 =''
        for i in s:
            if i.isalnum():
                s3 = s3 + i
        
        
        #seq[start:end:step]
        if s3[::].lower() == s3[::-1].lower():
            return True
        else:
            return False
    """        
    
