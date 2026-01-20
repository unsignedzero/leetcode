class Solution:
    def reverseWords(self, s: str) -> str:
        r""" One liner in Python. Split the current string, reverse all elements and join again.
        """
        return " ".join(reversed(s.split()))

