def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest_streak = 0
        for num in hset:
            if num-1 not in hset:
                current_num = num
                current_streak = 1
                while current_num+1 in hset:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        
        return longest_streak