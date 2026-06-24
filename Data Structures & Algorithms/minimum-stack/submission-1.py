class MinStack:


    def __init__(self):

        self._stack = []
        self._prefix_stack = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._prefix_stack) == 0:
            self._prefix_stack.append(val)
        else:
            self._prefix_stack.append(min(self._prefix_stack[-1], val))
        

    def pop(self) -> None:
        self._stack.pop()
        self._prefix_stack.pop()
        

    def top(self) -> int:
        return self._stack[-1]        

    def getMin(self) -> int:
        
        return self._prefix_stack[-1]