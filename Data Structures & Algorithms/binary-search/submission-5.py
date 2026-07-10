class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Third time is the charm with binary search

        # The theory behind binary search is really simple
        # Think of how you would search through a dictionary (the one for english for example)

        left, right = 0, len(nums) - 1

        while left <= right:
            # Use integer division to calculate the midpoint
            mid_point = (left + right) // 2

            if target < nums[mid_point]:
                right = mid_point - 1
            elif target > nums[mid_point]:
                left = mid_point + 1
            else:
                return mid_point
        return -1
