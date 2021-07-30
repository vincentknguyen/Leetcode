class Solution(object):
    def wordPattern(self, pattern, s):
            #Store the words
        #pattern = "abba", s = "dog cat cat dog" -> Output true

        #split -> splits the sentences into specific words
        words = s.split()
        #return words


        #the words cannot be the same pattern, if they are not the same length
        if len(words) != len(pattern):
            return False

        #Mapping dictionary as key-value pairs
            #pattern - words

        #start as a dictionary
        d = {}

        #s1 = "dog cat cat dog"

        #Go through each value
        for x in range(len(words)):
            
            
            #ex: pattern[0] = 'a'
            
            #check at each index, if it is in the dictionary
            if pattern[x] not in d:


                #condition that tells us that two patterns are not the same thing
                # "abba" = "dog dog dog dog" -> false
                if words[x]  in d.values():
                    return False
                
                #d['a'] = 'dog'
                #if not inside, add it into the dictionary
                d[pattern[x]] = words[x]


            else:
                #check if the word that first corresponds to what that pattern is
                #if d['a'] = 'dog' 
                
                if d[pattern[x]] != words[x]:
                    return False

        return True 
