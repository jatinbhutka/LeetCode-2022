# 159. Longest Substring with At Most Two Distinct Characters:

'''
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:
1 <= s.length <= 5 * 104
0 <= k <= 50
'''


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        windowStart = 0 
        freq = {}
        max_len = 0
        
        for windowEnd in range(len(s)):
            right = s[windowEnd]
            if right not in freq:
                freq[right] = 0
            freq[right] += 1
            
            while len(freq) > 2:
                left = s[windowStart]
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]
                windowStart += 1
            max_len = max(max_len, windowEnd - windowStart + 1)
        return max_len
            
            
          
          
# Time: O(N + N) ----> O(N) 
# space: O(2) ---> O(1)
