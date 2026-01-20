import random

class RandomizedSet:
    r""" We need to use both a map and list. The list is for random.choice
    as we cannot use that on a set. This is the error we get if we do.
    >> TypeError: 'set' object is not subscriptable

    The map is used as a 'set' to see what we have seen and then store the index
    as the value for the list so that makes deletes there faster.
    """

    def __init__(self):
        self.dataMap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.dataMap:
            return False

        self.dataMap[val] = len(self.data)
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:
        #print(f"Removing {val}. data {self.data} dataMap {self.dataMap}")
        if val not in self.dataMap:
            return False

        index = self.dataMap[val]
        # To delete, we rotate the element we want to move at the end.
        self.data[-1], self.data[index] = self.data[index], self.data[-1]
        # Update the map to the new value
        self.dataMap[self.data[index]] = index

        self.data.pop()
        self.dataMap.pop(val)
        return True

        #print(f"After Removing {val}. data {self.data} dataMap {self.dataMap}")

    def getRandom(self) -> int:
        return random.choice(self.data)

