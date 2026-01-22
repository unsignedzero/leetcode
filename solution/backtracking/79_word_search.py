from typing import List, Set, Tuple
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        wordLength = len(word)
        boardHeight = len(board)
        boardWidth = len(board[0])

        boardCount = Counter("".join("".join(x) for x in board))
        if Counter(word) - Counter(board):
            return False

        def getNeighors(currentState: Tuple[int]) -> List[Tuple[int]]:
            r""" Get's all possible neighbors. Can be optimized if we pass in seen to filter
            out invalid options
            """
            possibleState = []

            x, y = currentState

            if x + 1 < boardWidth:
                possibleState.append((x+1, y))
            if x - 1 >= 0:
                possibleState.append((x-1, y))
            if y + 1 < boardHeight:
                possibleState.append((x, y+1))
            if y - 1 >= 0:
                possibleState.append((x, y-1))

            return possibleState

        def checkBoard(board: List[List[str]], nextState: Tuple[int],
                       seen: Set[Tuple[int]], word: str, wordPosition: int) -> bool:
            r""" Brute force solution checking to see which tile is possible for the word sequence.
            """

            #print(f"Current state: {nextState}, seen: {seen}, wordPosition: {wordPosition}")
            if wordPosition == wordLength:
                return True

            # First scan
            if not nextState:
                for y in range(boardHeight):
                    for x in range(boardWidth):
                        if board[y][x] == word[wordPosition]:

                            # Catch if this is the only entry on the board
                            if wordPosition + 1 == wordLength:
                                return True

                            # We have a match get neighbors
                            currentPosition = (x, y)
                            possibleState = getNeighors(currentPosition)
                            newSeen = seen | set((currentPosition, ))

                            for eachPos in possibleState:
                                val = checkBoard(board, eachPos, newSeen, word, wordPosition + 1)
                                if val:
                                    return True
            # Secondary scans
            else:
                currentX, currentY = nextState
                if board[currentY][currentX] == word[wordPosition]:
                    newSeen = seen | set((nextState, ))

                    # Catch if this is the last entry on the board
                    if wordPosition + 1 == wordLength:
                        return True

                    possibleState = getNeighors(nextState)
                    for x, y in possibleState:
                        currentPosition = (x, y)
                        if currentPosition not in seen:
                            val = checkBoard(board, currentPosition, newSeen, word, wordPosition + 1)
                            if val:
                                return True
                else:
                    return False

            return False

        return checkBoard(board, None, set(), word, 0)

if __name__ == '__main__':
    solution = Solution()
    #print(solution.exist([["a", "a"]], "aa"))
    #print(solution.exist([["a"]], "a"))
    #print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    #print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

