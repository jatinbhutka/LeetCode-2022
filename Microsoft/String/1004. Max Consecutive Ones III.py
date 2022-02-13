# 1004. Max Consecutive Ones III:

"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        i = 0
        max_len = 0
        freq = {1:0, 0:0}
        maxfreq = freq[1]

        for j in range(len(arr)):
            right = arr[j]
            freq[right] += 1

            maxfreq = freq[1]

            while (j - i + 1) - maxfreq > k  :
                left = arr[i]
                freq[left] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
        return max_len
        
        
        
# Time Complexity:
#The above algorithm’s time complexity will be O(N), where ‘N’ is the count of numbers in the input array.

# Space Complexity:
#The algorithm runs in constant space O(1)       
