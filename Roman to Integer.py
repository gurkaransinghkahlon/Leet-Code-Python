class Solution:
    def romanToDecimal(self, S): 
        # code here
        res = 0
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        i=0
        while i<len(S):
            if (i+1)<len(S) and roman[S[i+1]] > roman[S[i]]:
                res += roman[S[i+1]] - roman[S[i]]
                i += 1
            else:
                res += roman[S[i]]
            
            i += 1
            
        return res