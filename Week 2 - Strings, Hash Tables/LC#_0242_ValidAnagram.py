"""
Dictionary solution
  Time: O(n)
  Space: O(n)
  
Smart solution:
  Time: O(n)
  Space: O(n)

"""

class Solution(object):
    def isAnagram(self, s, t):
        
        """
        #Smart way to do it: sorting        
        return sorted(s) == sorted(t)        
        """
        #Dictionary solution
        dict_s = {}        

            #Go through all strings of s, and store the counts in a dictionary
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1

            #decrement all occurences in the dictionary
        for j in t:
            if j in dict_s:
                dict_s[j] -= 1

                    #if it's decremented to
                if dict_s[j] == 0:
                    del dict_s[j]
            else:
                    #if the character j is NOT in the dictionary, return false
                return False

        #return dict_s
        #if you end up with an empty dictionary, return True. That means its an anagram

        if bool(dict_s) == False:
            return True
        else:
            return False                
        
            
            
        
            
            
                
