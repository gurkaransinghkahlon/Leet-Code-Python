class Solution:
    def transform(self, A, B): 
        #code here.
        if len(A) != len(B):
            return -1
        
        map = {}
        
        for char in  A:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
            
        for char in B:
            if char in map:
                map[char] -= 1
            else:
                map[char] = 1
        
        for count in map.values():
            if count != 0:
                return -1
        
        i,j = len(A)-1, len(B)-1
        c=0
        while(i>=0 and j>=0):
            if A[i] == B[j]:
                i -= 1
                j -= 1
            else:
                c += 1
                i -= 1
        
        return c