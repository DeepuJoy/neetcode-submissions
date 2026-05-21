class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique_nums = set(nums)
        longest_sequence = 0
        for val in nums:
            if val - 1 in nums:
                continue
            else:
                current_longest_sequence = 1
                while (True):

                    if val + current_longest_sequence in unique_nums:
                        current_longest_sequence += 1
                    else:
                        if current_longest_sequence > longest_sequence:
                            longest_sequence = current_longest_sequence
                        break
        return longest_sequence

                        
        
        