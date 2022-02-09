# 243. Shortest Word Distance:

"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
 
Constraints:
1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ind1 = -1
        ind2 = -1
        min_dis = float('inf')
        i = 0
        while i < len(wordsDict):
            if wordsDict[i] == word1:
                ind1 = i
            if wordsDict[i] == word2:
                ind2 = i
            if ind1 != -1 and ind2 != -1:
                min_dis = min(min_dis, abs(ind2 - ind1))
            i += 1
        return min_dis
      
      
# Complexity Analysis
# Time complexity: O(N * M), where N is the number of words in the input list, and M is the total length of two input words.
# Space complexity: O(1), since no additional space is allocated.      
