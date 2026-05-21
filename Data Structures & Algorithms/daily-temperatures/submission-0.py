class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        min_stack = []
        result = [0] * len(temperatures)

        for i, val in enumerate(temperatures):

            while min_stack and val > min_stack[-1][0]:
                stackVal, stackInd = min_stack.pop()
                result[stackInd] = i - stackInd
            min_stack.append((val, i))
        return result

        