class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Implement a version of binary search for this problem
        l , r = 0, len(nums) - 1
        res = nums[0]

        while (l <= r):
            # What if the portion is already sorted?
            if (nums[l] <= nums[r]):
                res = min(res, nums[l])
                break

            m = (r + l) // 2
            res = min(res, nums[m])
            if (nums[l] <= nums[m]):
                # Update the left pointer to be one past the mid pointer
                l = m + 1
            else:
                r = m - 1

        return res

                # [2,3,4,5,6,7,8,1] - 7 + 4 = 11 // 2 = 5
                # [7,8,1,2,3,4,5,6] - 
                    # map this out out
                    # 7, 2, 6 - 2
                    # 7, 8, 1 - 2
                    # 1, 1, 1 - 1
                    # 




        