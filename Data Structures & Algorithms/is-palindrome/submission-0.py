class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # This is a classic 2 pointer question
        # We need to initialise a left and right pointer
        # We need to then check if the value at the right and left pointer are identical when lower cased
        # If it in a non alphanumeric character - we need to skip it

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum(): # We need to do all the move in one go here, not via the larger loop, that is why we have nested loops
                left += 1
            
            while right > left and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
        
            left, right = left + 1, right - 1
        return True
