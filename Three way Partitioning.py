def threeWayPartition(self, array, a, b):
	    # code here 
        n=len(array)
        left = 0
        right = n-1
        i=0
        while i <=right:
            if array[i] < a:
                array[i],array[left] = array[left],array[i]
                left += 1
            elif array[i] > b:
                array[i],array[right] = array[right],array[i]
                right -= 1
                i -= 1
            i += 1