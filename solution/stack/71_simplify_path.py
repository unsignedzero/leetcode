class Solution:
    def simplifyPath(self, path: str) -> str:
        r""" Reduce the path to it's absolute path
        """

        finalOutput = []

        for eachSegment in path.split('/'):

            if eachSegment in ('.', ''):
                continue

            if eachSegment == '..':
                if finalOutput:
                    finalOutput.pop()
            else:
                finalOutput.append(eachSegment)

        # Re add back the slashes the path, including the leading one
        finalString = '/'.join(finalOutput)
        return f'/{finalString}'

if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("/.../solution/../b/c/../d/./"))
