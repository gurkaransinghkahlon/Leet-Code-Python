def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]

        left_sum = 0
        for i in range(len(nums)):
            if i!=0:
                left_sum += nums[i-1]
            if left_sum == total_sum - left_sum - nums[i]:
                return i

        return -1