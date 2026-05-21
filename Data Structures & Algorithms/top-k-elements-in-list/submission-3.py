class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # The length of the array is the max frequency
        # The brute force method is to have a hash map which counts the frequency and then returns the k highest frequency
        # The intelligent algorithm in this instance is the bucket sort algorithm
        # The bucket sort algorithm 

        frequency_count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            frequency_count[num] = 1 + frequency_count.get(num, 0)

        for key, value in frequency_count.items():
            buckets[value].append(key)

        results = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results
           
            

                