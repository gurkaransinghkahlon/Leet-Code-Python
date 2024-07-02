def areRotations(self,s1,s2):
        #code here
        if len(s1) != len(s2):
            return false
            
        combine = s1 + s1
        j=0
        for i in range(len(combine)):
            if j<len(s2) and combine[i] == s2[j]:
                j += 1
                
        return j == len(s2)
