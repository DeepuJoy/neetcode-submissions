class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Brute force initial solution
            # Iterate over the array and determine a frequency of each element

        # How can we do this in linear time?
        # Using the bucket sort algorithm and then we can do this
        # Create an input array
        frequency_buckets = [[] for i in range(len(nums) + 1)]
        frequency_map = {}
        top_k_frequent_items = k

        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)

        for n, c in frequency_map.items():
            frequency_buckets[c].append(n)

        result = []

        for i in range(len(frequency_buckets) - 1, 0, -1):
            if len(frequency_buckets[i]) > 0:
                result += frequency_buckets[i]
                top_k_frequent_items -= len(frequency_buckets[i])

            if top_k_frequent_items <= 0:
                return result







        

        


        





