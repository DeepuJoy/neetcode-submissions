class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False
        stack = []
        bracket_pairs = {'}':'{', ')':'(', ']':'['}
        

        for char in s:
            if char in bracket_pairs:
                if stack and stack[-1] == bracket_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

                


        