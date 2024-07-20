def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        i=0

        while i<=right and left <= right:
            if nums[i] == 0 and i>=left:
                self.swap(nums,i,left)
                left += 1

            elif nums[i] == 2:
                self.swap(nums,i,right)
                right -= 1

            else:
                i +=1 

    
    def swap(self,nums,i,j):
        nums[i],nums[j] = nums[j], nums[i]