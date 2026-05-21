class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)
        cum_mult = 1

        for i in range(1, len(nums)):
            cum_mult = cum_mult * nums[i - 1]
            output[i] = cum_mult

        cum_mult = 1

        for i in range(len(nums) - 2, -1, -1):
            cum_mult = nums[i + 1] * cum_mult
            output[i] *= cum_mult

        return output