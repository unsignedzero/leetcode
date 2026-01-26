from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    r""" Bad description on hasNext, which should be if the current node exists
    versus current node has next right. Works fine.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def hasNext(self) -> bool:
        #print(f"{self.root=}, {self.root.right=}")
        #from code import interact; interact(local=dict(globals(), **locals()))

        # Bad
        if self.root:
            return True
        else:
            return False

    def next(self) -> int:

        if not self.root:
            return None

        pointers = [self.root]

        while pointers[-1].left:
            pointers.append(pointers[-1].left)

        ptr = pointers[-1]
        if len(pointers) == 1:

            if ptr.right:
                self.root = ptr.right
            else:
                self.root = None
            return ptr.val

        else:

            rootPtr = pointers[-2]

            if not ptr.right:
               rootPtr.left = None
            else:
               rootPtr.left = ptr.right

            return ptr.val

if __name__ == '__main__':
    node20 = TreeNode(20)
    node9 = TreeNode(9)
    node15 = TreeNode(15, node9, node20)
    node3 = TreeNode(3)
    node7 = TreeNode(7, node3, node15)

    it = BSTIterator(node7)
    print(it.next())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())
    print(it.next())
    print(it.hasNext())


