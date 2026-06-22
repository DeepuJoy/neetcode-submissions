class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Do we need a frequency count? - Yes we do infact
        # I don't have a natural intuition for this problem...
        current_longest = 0
        l = 0
        frequency_map = {}

        for r in range(len(s)):

            frequency_map[s[r]] = frequency_map.get(s[r], 0) + 1
            while (r - l + 1) - max(frequency_map.values()) > k:
                
                frequency_map[s[l]] -= 1
                l += 1

            current_longest = max(current_longest, r - l + 1)

        return current_longest

            


            



        
        