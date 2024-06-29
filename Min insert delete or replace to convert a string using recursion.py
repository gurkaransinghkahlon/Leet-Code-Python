def editDistance(self, s, t):
		# Code here
        sArray = list(s)
        tArray = list(t)
        output = [[0]*(len(tArray)+1) for _ in range(len(sArray)+1)]
        
        for i in range(len(sArray)+1):
            output[i][len(tArray)] = len(sArray) - i;
            
        for j in range(len(tArray)+1):
            output[len(sArray)][j] = len(tArray) - j
            
        for i in range(len(sArray)-1,-1,-1):
            for j in range(len(tArray)-1,-1,-1):
                if sArray[i] == tArray[j]:
                    output[i][j] = output[i+1][j+1]
                    
                else:
                    output[i][j] = 1 + min(output[i][j+1], output[i+1][j], output[i+1][j+1])
                    
        
        return output[0][0]