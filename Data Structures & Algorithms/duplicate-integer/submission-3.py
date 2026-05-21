class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        
        for val in nums:
            if val in duplicates:
                return True
            duplicates.add(val)

        return False