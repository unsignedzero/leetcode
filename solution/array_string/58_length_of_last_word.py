class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r"""We just start at the end and count up what we see, ignoring
        white space.
        """

        wordLength = 0

        for char in s[::-1]:

            if char == ' ':
                if wordLength != 0:
                    return wordLength
            else:
                wordLength += 1

        return wordLength

