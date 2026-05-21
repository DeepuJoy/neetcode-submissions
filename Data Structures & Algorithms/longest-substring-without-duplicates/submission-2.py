class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        seen_chars = set()
        longest_substring = 0

        for r in range(len(s)):
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l += 1
            seen_chars.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)



        return longest_substring


        