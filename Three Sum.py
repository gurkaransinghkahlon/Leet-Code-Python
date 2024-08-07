def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i==0 or (i>0 and nums[i] != nums[i-1]):
                left = i+1
                right = len(nums)-1
                sum = 0-nums[i]

                while(left < right):
                    if sum == nums[left] + nums[right]:
                        res.append([nums[i], nums[left], nums[right]])
                        
                        while left<right and nums[left] == nums[left+1]:
                            left += 1
                        while left<right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1

                    elif nums[left]+ nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
                    
            
        return res