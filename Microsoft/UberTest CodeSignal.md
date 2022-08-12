# UberTest CodeSignal.md

<img width="1289" alt="image" src="https://user-images.githubusercontent.com/35987583/184329455-56107144-b77c-40dd-9540-ebe4f0865b59.png">
<img width="1302" alt="image" src="https://user-images.githubusercontent.com/35987583/184329497-78c97f52-ab18-486a-b1af-5f7e39cc6b5b.png">
<img width="1153" alt="image" src="https://user-images.githubusercontent.com/35987583/184329534-618c6528-6bdf-4076-80f9-f4db14977cfd.png">
<img width="961" alt="image" src="https://user-images.githubusercontent.com/35987583/184329567-38236121-287c-4d11-b9d2-1116e55bc044.png">


```python
def solution(s1, s2):
  
    # record appear times
    record1 = {}
    record2 = {}
    for ch in s1:
        record1[ch] = record1.get(ch,0)+1
    for ch in s2:
        record2[ch] = record2.get(ch,0)+1
    
    # merge with two pointers
    pt1 = 0
    pt2 = 0
    len1 = len(s1)
    len2 = len(s2)
    res = []
    while pt1 < len1 and pt2 < len2:
        if record1[s1[pt1]] < record2[s2[pt2]]:
            res.append(s1[pt1])
            pt1 += 1
        elif record1[s1[pt1]] > record2[s2[pt2]]:
            res.append(s2[pt2])
            pt2 += 1
        else:
            # if equal times
            if s1[pt1] <= s2[pt2]:
                res.append(s1[pt1])
                pt1 += 1
            elif s1[pt1] > s2[pt2]:
                res.append(s2[pt2])
                pt2 += 1
                
    # continue with the remaining characters
    while pt1 < len1:
        res.append(s1[pt1])
        pt1 += 1
    
    while pt2 < len2:
        res.append(s2[pt2])
        pt2 += 1
    return "".join(res)
```

<img width="987" alt="image" src="https://user-images.githubusercontent.com/35987583/184332426-0e7116fd-ca17-4c7a-8a91-9e043919462e.png">
<img width="978" alt="image" src="https://user-images.githubusercontent.com/35987583/184332466-5eeda018-83e9-437e-aa6e-dafb85a37120.png">


```python
import collections
def solution(a):
    tot = 0
    dic = collections.defaultdict(int)
    for i in range(len(a)):
        _str = str(a[i])
        n = len(_str)
        dic[n]+=1
    
    for i in  range(len(a)):
        for k,v in dic.items():
            tot+=a[i]*(v*pow(10,k))
        tot+=(a[i]*len(a))
    
    return tot
```
