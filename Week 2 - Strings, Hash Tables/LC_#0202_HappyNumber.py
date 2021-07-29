"""
https://leetcode.com/problems/happy-number/

Time: O(n)
Space: O(n)
"""



class Solution(object):
        
    def isHappy(self, n):
        
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
        
        return False
    
    
    def sumOfSquares(self,n):
        output = 0
        
    #There is a condition for while n:. The loop will iterate as long as there is an element in set n.
        while n:
            digit = n % 10
            digit = digit**2
            output = output + digit
            n = n //10
            
        #Return the output    
        return output
    
    
    

    
    
    
        
