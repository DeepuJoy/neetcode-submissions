class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # In this problem we need an intelligent mechanism of determining what an anagram is?
        # We need to make a dictionary 
            # The key of this dictionary will be a unique string or tuple that has the count of each letter in the letters' 
            # index position

            # The values in the dictionary will be the words from the list
            # Words with identical tuples keys will be grouped together

        anagram_groupings = defaultdict(list)
        
        for word in strs:

            index_count = [0] * 26

            for letter in word:
                index_count[ord(letter) - 97] += 1

            index_count_tuple = tuple(index_count)
            anagram_groupings[index_count_tuple].append(word)

        return list(anagram_groupings.values())

