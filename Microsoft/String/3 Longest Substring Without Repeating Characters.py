# 3. Longest Substring Without Repeating Characters:

"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        max_len = 0
        dic_index = {}
        
        for windowEnd in range(len(s)):
            right = s[windowEnd]
            if right in dic_index:
                windowStart = max(windowStart, dic_index[right] + 1)
            dic_index[right] = windowEnd
            max_len = max(max_len, windowEnd - windowStart + 1)
        return max_len
