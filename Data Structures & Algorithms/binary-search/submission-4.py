class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Use a 2 pointer approach - update the left and right pointer as you go through
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid_point = (l + r)//2
            if target < nums[mid_point]:
                r = mid_point - 1
            elif target > nums[mid_point]:
                l = mid_point + 1
            else:
                return mid_point

        return -1