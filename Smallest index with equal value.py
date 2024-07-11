def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        for i in range(len(nums)):
            if nums[i] == (i%10):
                res = i
                break

        return res