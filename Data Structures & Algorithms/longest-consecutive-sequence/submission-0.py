class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_sequence = 0
        next_num_exists = True

        for i in range(len(nums)):
            value = nums[i]
            current_max = 0
            while value in nums:
                value += 1
                current_max += 1
            
            if current_max > max_sequence:
                max_sequence = current_max
        
        return max_sequence
        
        