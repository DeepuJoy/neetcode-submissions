class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # What is the problem about?
            # Find the longest consecutive sequence in ana array but the values in the array do not have to in any kind of order

        # Can we use a hash set to simplify items like duplicates?

        deduplicated_nums = set(nums)

        largest_sequence = 0

        for val in nums:

            # the trick to this question is to understand how to properly track a sequence. 
            # n is the start of the sequence if n - 1 does not exist in the array.

            # WE might need to use a while loop as well in this as part of a solution

            if val - 1 not in deduplicated_nums:
                sequence_start = val
                current_sequence = 1
                while sequence_start + 1 in deduplicated_nums:
                    sequence_start += 1
                    current_sequence += 1
                
                if current_sequence > largest_sequence:
                    largest_sequence = current_sequence
                
        
        return largest_sequence            


