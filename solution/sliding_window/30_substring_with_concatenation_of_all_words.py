from collections import Counter, defaultdict
from operator import itemgetter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        sLength, wordLength = len(s), len(words[0])
        wordCount = Counter(words)
        returnIndexes = []

        # All words have the same length so we can check in "batches" where potential solutions
        # have subwords that ONLY occur in that batch
        for index in range(0, wordLength):

            wordsUsed = 0
            start = index
            window = defaultdict(int)

            # Increment by word length and check every possible word.
            for subIndex in range(index, sLength - wordLength + 1, wordLength):

                # Check if word exists
                word = s[subIndex:subIndex + wordLength]

                # The word does not exist so reject and retry again
                if word not in wordCount:
                    wordsUsed = 0
                    start = subIndex + wordLength
                    window = defaultdict(int)
                    continue

                # Found a valid word
                wordsUsed += 1
                window[word] += 1

                # We over match as we have counted a word too many times.
                while window[word] > wordCount[word]:
                    window[s[start:start + wordLength]] -= 1
                    wordsUsed -= 1
                    # Bring the left cursor forward
                    start += wordLength

                # We have found all words we watch to match
                if wordsUsed == len(words):
                    returnIndexes.append(start)
                    # We need to continue as there can be multiple matches

        return returnIndexes

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        r"""This is a brute-force solution to find all words as a substring
        in s. Workable but slow.
        """

        sLength = len(s)
        wordLength = len(words[0])
        wordCount = len(words)
        getAllFirstCharacter = set(map(itemgetter(0), words))

        currentPos = 0
        foundMatches = []

        while currentPos < sLength:
            currentChar = s[currentPos]

            if currentChar in getAllFirstCharacter:
                #print(f"First char match at {currentPos}")

                # Is it possible for the word to fit in the remaining s?
                if currentPos + (wordLength * wordCount) > sLength:
                    break

                # Iterate on possible matches
                wordsLeft = [x for x in words] # Make a new copy as we modify this

                # Search for start of words
                for wordListCount in range(wordCount):
                    #print(f"Looking at wordCount {wordListCount}")
                    hasMatch = False

                    nextChar = s[currentPos + wordLength * wordListCount]
                    possibleMatches = [x for x in words if x[0] == nextChar]

                    # Search within word
                    for newPos in range(1, wordLength):
                        index = currentPos + wordLength * wordListCount + newPos
                        nextChar = s[index]
                        newPossibleMatches = [x for x in possibleMatches if x[newPos] == nextChar]
                        if not newPossibleMatches:
                            break
                        possibleMatches = newPossibleMatches
                    else:
                        hasMatch = True

                    if hasMatch:
                        foundWord = possibleMatches[0]
                        if foundWord in wordsLeft:
                            wordsLeft.remove(foundWord)
                        else:
                            break

                        if not wordsLeft:
                            foundMatches.append(currentPos)
                    else:
                        break

            currentPos += 1

        return foundMatches

if __name__ == '__main__':
    solution = Solution()
