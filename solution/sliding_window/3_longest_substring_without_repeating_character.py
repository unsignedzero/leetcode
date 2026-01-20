class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r""" Here we keep two pointers, left and right to keep track of a window
        of what we seen We keep advancing right until we have something we already
        have seen and then advance left until it is not seen so we can guarantee
        everything is seen once.
        """

        lenString = len(s)
        # Trivial case for empty and one character string
        if lenString <= 1:
            return lenString

        leftPos, rightPos = 0, 1
        longestSubString = 1
        seen = set(s[0])

        while rightPos < lenString:
            #print(f"PTR: ({leftPos}, {rightPos})")
            newChar = s[rightPos]

            if newChar not in seen:
                #print(f"+Adding {newChar} to {seen}")
                seen.add(newChar)
                longestSubString = max(longestSubString, len(seen))

            else:
                # Advance the left position until we can insert the new char in
                while newChar in seen:
                    oldChar = s[leftPos]

                    #print(f"-Removing {oldChar} from {seen}")
                    seen.remove(oldChar)
                    leftPos += 1
                seen.add(newChar)

            rightPos += 1

        return longestSubString

if __name__ == '__main__':
    solution = Solution()
