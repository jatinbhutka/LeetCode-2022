# Rotation Count (medium):

<img width="1008" alt="image" src="https://user-images.githubusercontent.com/35987583/161219652-3ae8c455-1c2f-4f2e-83a2-5bccebec2a7b.png">

<img width="1002" alt="image" src="https://user-images.githubusercontent.com/35987583/161219696-398d7220-cb38-43fd-91df-1f71d9574df6.png">


```python
def count_rotations(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2

    # if mid is greater than the next element
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1

    # if mid is smaller than the previous element
    if mid > start and arr[mid - 1] > arr[mid]:
      return mid

    if arr[start] < arr[mid]:  # left side is sorted, so the pivot is on right side
      start = mid + 1
    else:  # right side is sorted, so the pivot is on the left side
      end = mid - 1

  return 0  # the array has not been rotated


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()
```

#### Time complexity:
Since we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.

#### Space complexity:
The algorithm runs in constant space O(1).


