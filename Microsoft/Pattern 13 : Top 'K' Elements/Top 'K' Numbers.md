# Top 'K' Numbers:

<img width="996" alt="image" src="https://user-images.githubusercontent.com/35987583/161373736-3aa690d7-cb5c-4d21-9ac2-31e213013062.png">
<img width="1009" alt="image" src="https://user-images.githubusercontent.com/35987583/161373740-2e106d7d-7284-482b-9aa6-92c5e25c031b.png">
<img width="998" alt="image" src="https://user-images.githubusercontent.com/35987583/161373750-f39899aa-8c99-4c6e-8529-3720e6714608.png">


```python
from heapq import *


def find_k_largest_numbers(nums, k):
  minHeap = []
  # put first 'K' numbers in the min heap
  for i in range(k):
    heappush(minHeap, nums[i])

  # go through the remaining numbers of the array, if the number from the array is bigger than the
  # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])

  # the heap has the top 'K' numbers
  return minHeap


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
```


#### Time complexity:
As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK)  which is asymptotically equal to O(N*logK)


#### Space complexity:
The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
