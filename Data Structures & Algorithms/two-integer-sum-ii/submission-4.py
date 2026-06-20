class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # This seems to be a very straight forward type of problem
        # If we assume the solution is 2 pointer - we can get to a solution very quickly

        # [a,b,c,d,e,f,g,h]
        #  |             |
        # We have a target, we can add the numbers in the target and if it is smaller, we move the right pointer to the left once
        # if it is bigger we move the left pointer to the right once.

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+ 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

                      
