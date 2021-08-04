class Solution(object):
    def hammingDistance(self, x, y):
        
        
        #Simple way
        #return bin(x^y)[2:].count('1')
        
        #1. Convert X and Y to binary
        #do a loop from x and y
        
        
        
        x, y = bin(x).replace('0b',''), bin(y).replace('0b','')
        nx, ny, counter = len(x), len(y), 0
        
        
        #zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
        if nx > ny:
            y = y.zfill(nx)            
        elif nx < ny:
            x = x.zfill(ny)
            
            
            
        for i in range(max(nx, ny)):
            if x[i]!=y[i]:
                counter += 1
        return counter
        
        #Number of positions at which the corresponding bits are different
        #return the hamming distance 
        
        #X = 1 -> #0 0 0 1
        #y = 4 -> #0 1 0 0 
                    #1   2
            
        #x = 3 ->  11
        #y = 1 ->   1
        #1
        
        
        
        
        
        
        
