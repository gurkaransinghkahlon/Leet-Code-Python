def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        expected_row = -1
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                expected_row = i
        
        if expected_row == -1:
            return False
        
        left, right = 0, len(matrix[expected_row])-1
        while left <= right:
            mid = (left+right)//2
            if target == matrix[expected_row][mid]:
                return True
            elif matrix[expected_row][mid] > target:
                right = mid-1
            else:
                left = mid+1

        return False