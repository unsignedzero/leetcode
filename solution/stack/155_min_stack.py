class MinStack:
    r""" The min stack using Pythons list as a stack.
    Oddly it's not much faster than the custom solution suggesting python
    is slow versus using standard libraries versus custom code.
    """

    def __init__(self):
        self.storage = []

    def push(self, val: int) -> None:
        self.storage.append(val)

    def pop(self) -> None:
        return self.storage.pop()

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return min(self.storage)

class MinStack2:
    r""" Using a list and manually processing it like a stack.
    """

    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, val: int) -> None:
        self.size += 1
        self.storage.append(val)

    def pop(self) -> None:
        value = self.storage[self.size - 1]
        del self.storage[self.size - 1]
        self.size -= 1
        return value

    def top(self) -> int:
        return self.storage[self.size - 1]

    def getMin(self) -> int:
        return min(self.storage)

