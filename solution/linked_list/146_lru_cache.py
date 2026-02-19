from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Node:
    r""" Used for doubly-linked list
    """
    EMPTY_VALUE: ClassVar[int] = -1

    key: int = EMPTY_VALUE
    value: int = EMPTY_VALUE
    previousNode: Node = None
    nextNode: Node = None

    def __str__(self) -> str:
        return f"({self.key}, {self.value})"

class LRUCache:
    r""" We keep a doubly-linked list for keeping which element is "latest"
    and use a map for O(1) for fetching the node.
    """

    def __init__(self, capacity: int):
        self.internalMap = dict() # This will be a mapping of value -> node

        self.newestNode = self.oldestNode = None

        self.MAX_SIZE = capacity
        self.size = 0

    def __str__(self) -> str:
        currentNode = self.newestNode
        stringBuffer = []

        while currentNode:
            stringBuffer.append(str(currentNode))
            currentNode = currentNode.nextNode

        currentList = " -> ".join(stringBuffer)
        stringBuffer.clear()

        for k, v in sorted(self.internalMap.items()):
            stringBuffer.append(f"({k}, {v})")

        currentMap = ", ".join(stringBuffer)

        return f"list: [{currentList}]; map: ({currentMap})"

    def _insert_new_node(self, newNode: Node) -> None:

        oldNewNode = self.newestNode
        if oldNewNode:
            oldNewNode.previousNode = newNode
            newNode.nextNode = oldNewNode

        self.newestNode = newNode
        self.internalMap[newNode.key] = newNode

        if not self.oldestNode:
            self.oldestNode = newNode

    def _remove_last_node(self) -> None:
        lastNode = self.oldestNode
        previousNode = lastNode.previousNode
        self.oldestNode = previousNode

        if self.newestNode == lastNode:
            self.newestNode = None

        if previousNode:
            previousNode.nextNode = None
        lastNode.previousNode = lastNode.nextNode = None
        del self.internalMap[lastNode.key]

    def _update_node(self, newNode: Node) -> None:

        # We got the latest node
        if self.newestNode == newNode:
            return

        # Get neighboring nodes
        previousNode, nextNode = newNode.previousNode, newNode.nextNode

        # If the node we get is the first node, nothing changes
        if not previousNode:
            return

        # If what we get is the last node
        elif not nextNode:
            self.oldestNode = previousNode
            previousNode.nextNode = None

        # We get some node in the body
        else:
            previousNode.nextNode = nextNode
            nextNode.previousNode = previousNode

        # Move the node "up" to the latest node
        self._insert_new_node(newNode)

    def get(self, key: int) -> int:
        returnNode = self.internalMap.get(key, Node)
        returnValue = returnNode.value

        # We have a valid result
        if returnValue != Node.EMPTY_VALUE:
            self._update_node(returnNode)

        return returnValue

    def put(self, key: int, value: int) -> None:

        # Check initial state
        if self.newestNode is None and self.oldestNode is None:
            newNode = Node(key, value)
            self.newestNode = self.oldestNode = newNode
            self.internalMap[key] = newNode
            self.size += 1
            return

        returnNode = self.internalMap.get(key, Node)
        # If value already exists
        if returnNode.value != Node.EMPTY_VALUE:
            # Update the value if we see same key but new value
            returnNode.value = value
            self._update_node(returnNode)
            return

        # Else we add it in
        newNode = Node(key, value)
        if self.MAX_SIZE > self.size:
            self.size += 1
        else:
            self._remove_last_node()

        self._insert_new_node(newNode)

def case1():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    lRUCache.get(1)     # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    lRUCache.get(2)     # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lRUCache.get(1)     # return -1 (not found)
    lRUCache.get(3)     # return 3
    lRUCache.get(4)     # return 4

def case6():
    r""" Dealing with edge cases of LRU of size 1
    """

    lRUCache = LRUCache(1)
    lRUCache.put(2, 1)
    lRUCache.get(1)
    lRUCache.put(3, 2)
    lRUCache.get(2)
    lRUCache.get(3)

def case14():
    r""" Need to make sure to update the entry if we see it.
    """
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(2, 2)
    lRUCache.get(2)
    lRUCache.put(1, 1)
    lRUCache.put(4, 1)
    lRUCache.get(2)

if __name__ == '__main__':
    pass
