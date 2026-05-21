class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique_nums = set(nums)
        longest_sequence = 0
        for val in nums:
            if val - 1 not in nums:
                current_longest_sequence = 1

                while (val + current_longest_sequence in unique_nums):
                    current_longest_sequence += 1

                longest_sequence = max(longest_sequence, current_longest_sequence)
        
        return longest_sequence

                        
        
        