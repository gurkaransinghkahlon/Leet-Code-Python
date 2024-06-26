 def ispar(self,x):
        # code here
        n = -1
        while(len(x) != n):
            n = len(x)
            x = x.replace("()","")
            x = x.replace("{}","")
            x = x.replace("[]","")
        
        return len(x) == 0