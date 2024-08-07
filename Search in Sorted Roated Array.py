def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums)-1
        while(left < right):
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
            
        start = left
        left, right = 0, len(nums)-1

        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start-1

        while(left <= right):
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        
        return -1