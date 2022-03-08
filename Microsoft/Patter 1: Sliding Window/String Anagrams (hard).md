# String Anagrams (hard):

Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc 

acb 

bac 

bca 

cab 

cba 

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

```
Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
```
```
Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
```


```python
def find_string_anagrams(s, p):
  char_freq ={}
  for ch in p:
      if ch not in char_freq:
          char_freq[ch] = 0
      char_freq[ch] += 1
            
  res = []
  window_start = 0
  match = 0
  
  for window_end in range(len(s)):
      right = s[window_end]
      
      # Check If right in freq:
      if right in char_freq:
          char_freq[right] -= 1
          
          # if right freq == 0, Increase match += 1
          if char_freq[right] == 0:
              match += 1    
      
      # If match == len(char_freq): append window_start
      if match == len(char_freq):
          res.append(window_start)
          
      if window_end >= len(p) - 1:
          left = s[window_start]
          window_start += 1
          
          if left in char_freq:
              if char_freq[left] == 0:
                  match -= 1
              char_freq[left] += 1
              
  return res



```
