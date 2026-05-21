class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # An anagram has the exact same count of letters
        # For each character in one string we can add number
        # For each character in another string, we can subtract the count
        # For an anagram the end count should be 0?
        character_count = {}

        for char in s:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

        for char in t:
            if char in character_count:
                character_count[char] -= 1
            else:
                return False

        # Assuming we get here - iterate through the hshmap and see if count is 0
        for char in character_count:
            if character_count[char] != 0:
                return False
        
        return True
            


