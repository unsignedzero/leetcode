import itertools
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        r""" This is a simplified solution listed on Leetcode.
        """

        resultBuffer, currentBuffer, letterCount = [], [], 0
        for word in words:
            lenWords = len(word)

            # We overflow and need to add in a new line
            if letterCount + lenWords + len(currentBuffer) > maxWidth:
                for index in range(maxWidth - letterCount):
                    currentBuffer[ index % (len(currentBuffer) - 1 or 1)] += ' '
                resultBuffer.append(''.join(currentBuffer))
                currentBuffer, letterCount = [], 0

            currentBuffer += [word]
            letterCount += lenWords

        if currentBuffer:
            flattenedBuffer = ' '.join(currentBuffer)
            charactersUsed = len(flattenedBuffer)
            deltaWhiteSpace = maxWidth - charactersUsed
            whiteSpaceBuffer = ' ' * deltaWhiteSpace

            resultBuffer.append(f"{flattenedBuffer}{whiteSpaceBuffer}")

        return resultBuffer

    def interweave(self, leftStrList: List[str], rightStrList: List[str]) -> List[str]:
        r""" This interweaves the input word list with the white space list.
        """

        return [x for x in itertools.chain.from_iterable(itertools.zip_longest(leftStrList, rightStrList)) if x is not None]

    def generateWhiteSpaces(self, whiteSpaceCount: int, whiteSpacePockets) -> List[str]:
        r""" Calculates the amount of white space we need to add in.
        """

        #print(f"Generating white space count: {whiteSpaceCount}, pockets: {whiteSpacePockets}")
        # No pockets, i.e. one word so fill in the remaining needed
        if whiteSpacePockets == 0:
            return [' ' * whiteSpaceCount]
        # If it's easily divisible, we distribute it equally to all spots.
        elif whiteSpaceCount % whiteSpacePockets == 0:
            return [' ' * (whiteSpaceCount//whiteSpacePockets) for _ in range(whiteSpacePockets)]
        else:
            # We are greedy and add the extra 1 space so we use up the rest of the row
            whiteSpace = []
            remainingWhiteSpace = whiteSpaceCount % whiteSpacePockets
            minWhiteSpace = whiteSpaceCount // whiteSpacePockets
            #print(f"minWhiteSpace: {minWhiteSpace}, remainingWhiteSpace: {remainingWhiteSpace}")
            for _ in range(whiteSpacePockets):
                if remainingWhiteSpace:
                    whiteSpace.append(' ' * (minWhiteSpace + 1))
                    remainingWhiteSpace -= 1
                else:
                    whiteSpace.append(' ' * minWhiteSpace)

        return whiteSpace

    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:
        r""" Original solution following what needs to be done for text justification
        """
        output = []
        currentLine = []
        currentCharLeft = maxWidth
        whiteSpacePockets = 0

        for eachWord in words:
            lenWord = len(eachWord)
            #print(f"lenWord: {lenWord}, currentCharLeft: {currentCharLeft} word: {eachWord} buffer: {currentLine}")

            # Can we fit the word in the current string?
            if (currentCharLeft - lenWord) >= whiteSpacePockets:
                currentLine.append(eachWord)
                currentCharLeft -= lenWord
                whiteSpacePockets += 1

            # Else update the output for a new line and add it in
            else:
                whiteSpace = self.generateWhiteSpaces(currentCharLeft, whiteSpacePockets - 1)
                fullLine = self.interweave(currentLine, whiteSpace)
                #print(f"whiteSpace: {whiteSpace}, fullLine: {fullLine}")
                output.append("".join(fullLine))

                currentLine = [eachWord]
                whiteSpacePockets = 1
                currentCharLeft = maxWidth - lenWord

        if currentLine:
            whiteSpace = [' ' for _ in range(whiteSpacePockets - 1)]
            currentCharLeft -= len(whiteSpace)
            whiteSpace.append(' ' * currentCharLeft)

            fullLine = self.interweave(currentLine, whiteSpace)
            output.append("".join(fullLine))

        return output

if __name__ == '__main__':
    solution = Solution()
    #print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    #print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","solution","computer.","Art","is","everything","else","we","do"], 20))

