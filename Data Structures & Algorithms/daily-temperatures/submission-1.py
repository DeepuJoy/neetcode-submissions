class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Goals
            # Shower  - Done
            # Eat dinner - 30 mins total - Done
            # 2 Leet code problems - 40 mins
        # Input array comes in with temperatures where temperatures[i] is the temperature on the ith day.
        # Return an array where the 
        
        # Look into what a monotonic stack is meant to be:

            # Read 20 pages

        stack = [] # We are going to store the element and its index in the stack - the stack must always be in decreasing order
        indicies = [0] * len(temperatures) 

        for i, val in enumerate(temperatures):
            
            while stack and  val > stack[-1][1]:

                # We need to now pop off the stack
                stackI, stackV = stack.pop()
                indicies[stackI] = i - stackI

            stack.append([i, val])

        return indicies

        