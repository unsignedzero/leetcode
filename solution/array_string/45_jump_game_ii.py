from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        r"""This is a one sweep where we go left to right and see how far our jumps
        can make it. If we exhaust all options we increment again and go.
        """

        elementCount = len(nums) - 1
        currentJumpIndex = farthestJumpIndex = jumpCount = 0

        for index in range(elementCount):
            farthestJumpIndex = max(farthestJumpIndex, nums[index] + index)

            if index == currentJumpIndex:
                jumpCount += 1
                currentJumpIndex = farthestJumpIndex
        return jumpCount


    def jump2(self, nums: List[int]) -> int:
        r"""Brute force BFS solution where we try to keep every board state to calculate a
        possible route
        """

        # State
        step = 1

        currentState = [nums]
        while currentState:
            newState = []

            for currentBoard in currentState:
                possibleJump = currentBoard[0]
                if possibleJump > 0:
                    for jumpValue in range(1, possibleJump + 1):
                        newBoard = currentBoard[jumpValue:]
                        if len(newBoard) == 1:
                            return step
                        newState.append(newBoard)
            step += 1
            currentState = newState

        return step

