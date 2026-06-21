class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # This seems like the problem a 2 pointer solution was meant to try and solve:
        # Basically need to calculate all the possible areas and return the largest

        l, r = 0, len(heights) - 1
        max_area = 0
        # [1,7,2,5,4,7,3,6]
        while l < r:
            cur_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(cur_area, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area




        