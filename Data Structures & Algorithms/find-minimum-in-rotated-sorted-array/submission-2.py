class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find minimum in rotated sorted array

        # This is a very interesting problem - we can easily find the minimum becuase it has been rotated.
        # The easiest way to do this is to check the first instance when the next value is less than the previous value.
        # This wiould be the trivial way to do it.
        res = nums[0] 
        left, right = 0, len(nums) - 1

        while left <= right:

            # Check the scenario when the list is fully rotated
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid_point = (right + left) // 2
            
            # Remember the midpoint is what we use in binary search to eventually be our value
            # We need to return the smallest value in the array ultimately
            res = min(res, nums[mid_point])

            
            if  nums[left] <= nums[mid_point]:
                left = mid_point + 1
            else:
                right = mid_point - 1
        
        return res



        