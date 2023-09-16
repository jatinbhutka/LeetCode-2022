# 910 Smallest Range II:


<img width="876" alt="image" src="https://github.com/jatinbhutka/LeetCode-2022/assets/35987583/23dba814-f169-4f60-9b49-5d4a94d0627c">
<img width="856" alt="image" src="https://github.com/jatinbhutka/LeetCode-2022/assets/35987583/3e26f6aa-de39-491d-a509-9eeb54913c96">
<img width="864" alt="image" src="https://github.com/jatinbhutka/LeetCode-2022/assets/35987583/ed681ec9-57d5-48c2-b35a-dfc7643ecdaa">

<img width="271" alt="image" src="https://github.com/jatinbhutka/LeetCode-2022/assets/35987583/661ec9cb-a7cc-4fce-aad8-7783ead7ee45">

```python
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        if len(nums) <= 1:
            return 0

        nums.sort()
        min_num = nums[0]
        max_num = nums[-1]

        result = max_num - min_num

        for i in range(len(nums) - 1):
            num1, num2 = nums[i], nums[i+1]

            maxAfter = max( nums[i] + k, nums[-1] - k)
            minAfter = min(nums[i+1] - k, nums[0] + k)

            score = maxAfter - minAfter
            result = min( result, score )

        return result
```

# TIme: O(N Log N)
# space: O(1)
