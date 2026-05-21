class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 1
        end = len(numbers)

        while start < end:
            result = numbers[start - 1] + numbers[end - 1]
            if result > target:
                end -= 1
            elif result < target:
                start += 1
            else:
                return [start, end]

        