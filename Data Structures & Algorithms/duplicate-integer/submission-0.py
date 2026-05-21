class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_count = {}
        for i in range(len(nums)):
            if nums[i] in seen_count:
                return True
            seen_count[nums[i]] = 1
        return False
        