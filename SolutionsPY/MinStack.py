class MinS:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.helper=[]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.helper.append(x)
        self.helper.sort()

    def pop(self) -> None:
        for i in self.helper:
            if i == self.stack[-1]:
                self.helper.remove(i)
                break
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[0]