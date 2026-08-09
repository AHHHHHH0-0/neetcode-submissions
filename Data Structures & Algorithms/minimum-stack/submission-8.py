class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
        else:
            self.stack.append(val-self.minimum)
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        if self.stack:
            pop = self.stack.pop()
            if not self.stack:
                self.minimum = float('inf')
            elif pop < 0:
                self.minimum -= pop

    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            if top < 0 or len(self.stack)==1:
                return self.minimum 
            else:
                return self.minimum + top

    def getMin(self) -> int:
        if self.stack:
            return self.minimum
