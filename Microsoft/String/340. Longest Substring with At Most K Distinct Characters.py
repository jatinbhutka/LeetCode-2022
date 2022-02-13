# 340 Longest Substring with At Most K Distinct Characters:

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
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        freq = {}
        windowStart = 0
        for windowEnd in range(len(s)):
            right = s[windowEnd]
            if right not in freq:
                freq[right] = 0
            freq[right] += 1
            
            while len(freq) > k:
                left = s[windowStart]
                freq[left] -= 1
                if freq[left] == 0:
                    del freq[left]
                windowStart += 1

            max_len = max(max_len, windowEnd - windowStart + 1)
        return max_len
      
'''      
Time Complexity: O(N + N) ---> O(N) 
The above algorithm’s time complexity will be O(N), where N is the number of characters in the input string. The outer for loop runs for all characters, and the inner while loop processes each character only once; therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).

Space Complexity: O(K)
The algorithm’s space complexity is O(K), as we will be storing a maximum of K+1 characters in the HashMap.      
'''
