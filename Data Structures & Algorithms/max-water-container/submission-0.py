class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = 1
        max_area = 0
        while (l < len(heights) - 1):
            current_area = min(heights[l], heights[r]) * (r - l)
            if current_area > max_area:
                max_area = current_area
            
            if (r == len(heights) - 1):
                l += 1
                r = l + 1
            else:
                r += 1

        return max_area
            

            
        