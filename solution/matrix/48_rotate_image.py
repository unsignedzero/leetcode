from typing import List

class Solution:
    def ceiling_division(self, n, d):
        return -(n // -d)

    def rotate(self, matrix: List[List[int]]) -> None:
            cols = len(matrix) - 1
            rows = len(matrix[0]) - 1

            if len(matrix) == 1:
                return matrix

            for x in range(self.ceiling_division(rows + 1, 2)):
                for y in range((cols+1) // 2):
                    #print(f"({x},{y}) -> ({cols-y},{x}) -> ({rows-x},{cols-y}) -> ({y},{rows-x})")
                    #matrix[x][y], matrix[cols-y][x], matrix[rows - x][cols - y], matrix[y][rows-x]
                    matrix[x][y], matrix[cols-y][x], matrix[rows - x][cols - y], matrix[y][rows-x] = matrix[cols-y][x], matrix[rows - x][cols - y], matrix[y][rows-x], matrix[x][y]

if __name__ == '__main__':
    solution = Solution()
    #matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2],[3,4]]
    print(solution.rotate(matrix))
    print(matrix)
