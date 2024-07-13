def get_min_max(self, arr):
        mini, maxi = float('inf'), float('-inf')
        i=0
        n = len(arr)
        while i < n:
            mini = min(mini,arr[i])
            maxi = max(maxi,arr[i])
            i += 1
            
        return (mini,maxi)