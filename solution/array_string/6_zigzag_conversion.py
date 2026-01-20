from itertools import cycle

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r"""With the zigzag pattern, we generate one vertical line and then count
        "up" to the next column. This yields the repeated pattern. All the
        '1s' are grouped in the row and concatenated until we work on row 2 and so on...

        k = 1:
        1 1 1

        k = 2:
        1 /1 /1
        2/ 2/ 2

        k = 3:
        1  /1  /1
        2 2 2 2 2
        3/  3/  3

        ...
        As such we can move the strings in the right 'row' and combine them. We
        use cycle to get infinite cycles to position each char into the right spot
        before combining them back into the new output string.
        """

        if numRows == 1:
            return s

        # Initialize result
        result = []
        for _ in range(numRows):
            result.append([])

        # Generate the infinite cycle so we can freely index forever
        leftCycle = list(range(1, numRows + 1))
        rightCycle = list(range(numRows - 1, 1, -1))
        indexCycle = cycle(leftCycle + rightCycle)
        #print(f"Cycle group {leftCycle + rightCycle}")

        # Read the output into the right format
        for index, char in zip(indexCycle, s):
            result[index-1].append(char)
        #print(f"Storage {result}")

        # Combine the list of lists together.
        return "".join("".join(x) for x in result)


if __name__ == '__main__':
    solution= Solution()
    print(solution.convert("PAYPALISHIRING", 3))
