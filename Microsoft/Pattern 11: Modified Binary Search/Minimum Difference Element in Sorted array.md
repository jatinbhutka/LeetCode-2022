# Minimum Difference Element in Sorted array.md

<img width="989" alt="image" src="https://user-images.githubusercontent.com/35987583/161224581-b8df4926-b524-4b67-8580-5ce82be5cd9a.png">

```python
def search_min_diff_element(arr, key):
  if key < arr[0]:
    return arr[0]
  n = len(arr)
  if key > arr[n - 1]:
    return arr[n - 1]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      return arr[mid]

  # at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array
  # return the element which is closest to the 'key'
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]
  return arr[end]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()

```

### Time: O(log N)
### Space: O(1)
