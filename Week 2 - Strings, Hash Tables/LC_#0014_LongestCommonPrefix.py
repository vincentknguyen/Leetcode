

"""
Time: O(n^2)
Space: O(n)

https://leetcode.com/problems/longest-common-prefix/

"""


class Solution(object):
    def longestCommonPrefix(self,strs):
        shortest_word_len = len(min(strs,key = len))
        prefix = ''

        #iterate through each index
        for i in range(0,shortest_word_len):
            letter = strs[0][i]

            for word in strs[1:]:
                if word[i] != letter:
                    return prefix

            #append the letter, before looping to the next letter
            prefix = prefix + letter

        return prefix
    
    """
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        n = len(strs)
        com = []
        
        min_len = min(map(len, strs))
        
        for i in range(min_len):
            if len(set([s[i] for s in strs])) == 1:
                com.append(strs[0][i])
            else:
                break
        
        return ''.join(com)
        #return com
    """   

