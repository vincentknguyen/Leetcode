"""
https://leetcode.com/problems/valid-perfect-square/

"""

class Solution(object):
    def isPerfectSquare(self, num):
       
        #perfect square means that
        #x^2 == 1
        
        # O(log n) Solution ->  With binary search
        
        l, r = 0, num
        
        while (l <= r):
            
            mid = (l+r) //2
            squared = mid ** 2
            
            if num == squared:
                return True
            elif squared < num:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
        
    
        # O(n) Solution ->  Without binary search
        """
        x = 1
        square = 1
        while square <= num:
            
            square = x*x
            if square == num:
                return True
            
            x += 1
        
        return False
        """
          
        
        
