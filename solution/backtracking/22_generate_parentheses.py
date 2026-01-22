from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r""" Simpler problem keeping track of # of open/closed parenthesis
        """

        result = []
        FINAL_LENGTH = 2 * n

        def generateStep(openCount: int, closedCount: int, currentStr: str):
            if (openCount + closedCount) == FINAL_LENGTH:
                result.append(currentStr)
                return

            if openCount < n:
                generateStep(openCount + 1, closedCount, f"{currentStr}(")
            if openCount > closedCount:
                generateStep(openCount, closedCount + 1, f"{currentStr})")

        generateStep(0, 0, '')
        return result

    def generateParenthesis2(self, n: int) -> List[str]:
        r""" Weirdly order matters here so larger solutions just fail.
        Simple brute force solution.
        """

        result = set()

        def generateStep(depth: int, currentStr: str):
            if depth > 0:
                generateStep(depth - 1, f"(){currentStr}")
                generateStep(depth - 1, f"({currentStr})")
                generateStep(depth - 1, f"{currentStr}()")
            else:
                result.add(currentStr)

        generateStep(n, '')

        return list(result)

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(4))
