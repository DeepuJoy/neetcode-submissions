class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store the required number and the required number 
        # To meet the target as key value pairs in a hashmap
        store = {}

        # 3,4,5,6 - target = 7
            # 3, 0
            # -3, 1
            # 5, 2
        # Implement the hashmap solution to this
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store:
                return [store[diff], i]
            else:
                store[nums[i]] = i



        