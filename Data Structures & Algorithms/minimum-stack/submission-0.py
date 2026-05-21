class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum_stack) == 0 or val < self.getMin():
            self.minimum_stack.append(val)
        else:
            self.minimum_stack.append(self.minimum_stack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # This returns in the minimum in o(n) time
        return self.minimum_stack[-1]     
