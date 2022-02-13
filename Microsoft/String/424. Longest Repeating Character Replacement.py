# 424. Longest Repeating Character Replacement:
'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_len = 0
        freq = {}
        maxfreq = 0
        
        
        for j in range(len(s)):
            right = s[j]
            if right not in freq:
                freq[right] = 0
            freq[right] += 1
            
            maxfreq = max(maxfreq, freq[right])
            
            while (j - i + 1) - maxfreq > k:
                left = s[i]
                freq[left] -= 1
                i += 1
            max_len = max(max_len, j - i +1)
        return max_len
      
      
# Time: O(N + N) ---> O(N)
# Space: O(k)


# Time Complexity:
#The above algorithm’s time complexity will be O(N), where ‘N’ is the number of letters in the input string.

# Space Complexity:
# As we expect only the lower case letters in the input string, we can conclude that the space complexity will be O(26) to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).
