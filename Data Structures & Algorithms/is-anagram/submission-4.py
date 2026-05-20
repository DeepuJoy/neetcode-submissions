class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Initialise 2 arrays of 26 length of 0's
        # iterate over s and t and increment the position of ord(s[i]) and ord(t[i])
        # compare the 2 arrays at the end
        
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - 97] += 1
            count[ord(t[i]) - 97] -= 1

        return count == [0] * 26



        
        