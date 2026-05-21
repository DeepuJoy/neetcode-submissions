class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a hashmap which holds all the anagrams together
        anagrams = defaultdict(list)

        for word in strs:

            # Create a count of each letter in each word
            count_list = [0] * 26

            for char in word:

                index = ord(char) - 97
                count_list[index] += 1
            
            # convert the numbers into something which can be a key in a hashmap
            count_key = tuple(count_list)
            if count_key in anagrams:
                anagrams[count_key].append(word)
            else:
                anagrams[count_key] = [word]

        
        return list(anagrams.values())





        