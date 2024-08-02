def nextSmaller(self,arr, N):
        nextSmall = [0]*N 
        stack = [-1]
        for i in range(N-1,-1,-1):
            while stack[-1] != -1 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nextSmall[i] = stack[-1]
            stack.append(i)

        return nextSmall

    def prevSmaller(self,arr,N):
        prevSmall = [0]*N
        stack = [-1]
        for i in range(N):
            while stack[-1] != -1 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prevSmall[i] = stack[-1]
            stack.append(i)
        return prevSmall
 
    def maxAreaInHistogram(self,histogram, N):
        prevSmall = self.prevSmaller(histogram,N)
        nextSmall = self.nextSmaller(histogram,N)
        maxArea = 0
        for i in range(N):
            if nextSmall[i] == -1:
                nextSmall[i] = N
            area = (nextSmall[i] - prevSmall[i] - 1)*histogram[i]
            maxArea = max(area, maxArea)

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histogram = [0]*len(matrix[0])
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    histogram[j] += 1
                else:
                    histogram[j] = 0

            area = self.maxAreaInHistogram(histogram,len(histogram))
            maxArea = max(area,maxArea)

        return maxArea