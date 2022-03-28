# 784. Letter Case Permutation


<img width="853" alt="image" src="https://user-images.githubusercontent.com/35987583/160384977-c17de023-321f-4c7e-b63e-277141f4ded6.png">


```python
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutation = []
        permutation.append(s)
        
        for i in range(len(s)):
            if s[i].isalpha():
                
                for j in range(len(permutation)):
                    set1 = list(permutation[j])
                    set1[i] = set1[i].swapcase()
                    permutation.append("".join(set1))
        return permutation
```


#### Time complexity:
Since we can have 2^N permutations at the most and while processing each permutation we convert it into a character array, the overall time complexity of the algorithm will be O(N*2^N)


#### Space complexity:
All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) permutations, the space complexity of our algorithm is O(N*2^N)
