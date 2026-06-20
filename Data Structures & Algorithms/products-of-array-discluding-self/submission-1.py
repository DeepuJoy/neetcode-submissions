class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 2 Pass solution attempt - create a cumulative multiplication for forwards and then do it backwards.
        # This should use 2 loops, each with a single iteration - therefore, we get O(n) time complexity.

        product_array = [1] * len(nums)
        cum_mult = 1

        # In the right hand pass store the cumulative multiplication of all values nums[i]
        for i in range(1,len(nums)):
            cum_mult *= nums[i - 1]
            product_array[i] = cum_mult
            
        # [a,b,c,d,e,f]
        # [1,a * cum_mult, a*cum_mult*b...]

        # On the other end we need to do a reverse pass of the array

        cum_mult = 1
        for i in range(len(nums) - 2, -1, -1):
            cum_mult *= nums[i + 1]
            product_array[i] *= cum_mult # the key here is we need to multiply on the way out

        return product_array

