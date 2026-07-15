class Solution:
    def findMin(self, nums: List[int]) -> int:

        # In this problem we need to use binary search but instead we
        # need to change the condition we use to implement binary search. 

        l, r = 0, len(nums) - 1
        res = nums[0]


        while l <= r:

            # What if the array is rotated 0 times?

            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break


            # l starts at one end of the array
            # r starts at the other end of the array
            
            m = (l + r) // 2

            # We know there will be two sorted sections of the array
            # We will know the left is sorted if nums[l] < nums[m]
            # We will know the right is sorted if nums[m] > nums[r]
            # We know the minimum will be in the side where the array is not sorted
            
            # If the left is sorted we no longer want to look there
            # If the right is sorted we no longer want to look there

            # The result we want to update is going to be the minium of the current result
            # and the newly calculated midpoint in the search space

            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                # The left is sorted

                l = m + 1
            else:
                # the right is sorted

                r = m - 1

        return res

        