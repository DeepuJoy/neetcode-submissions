class Solution:
    def isValid(self, s: str) -> bool:

        # Probably not required to design a stack here

        stack = []
        closeToOpen = {"}":"{", ")": "(", "]":"["}


        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # Remember you can only look at the top value of a stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False





        