class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r"""Search and find the first occurrence in the string
        """

        lenHaystack, lenNeedle = len(haystack), len(needle)
        firstLetterNeedle = needle[0]

        for position, firstChar in enumerate(haystack):
            if firstChar == firstLetterNeedle:
                #print(f"Left {haystack[position:position + lenNeedle]} Right {needle}")
                # Check if the full string matches
                if haystack[position:position + lenNeedle] == needle:
                    return position

        return -1

