Problem Statement #
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

```
Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.
Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.


```

```python
def can_attend_all_appointments(intervals):
  
  intervals.sort(key = lambda x : x[0])
  
  if len(intervals)<=1:
    return True
  
  start = intervals[0][0]
  end = intervals[0][1]
  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval[0] < end:
      return False
    start = interval[0]
    end = interval[1]
  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()
```

# Time complexity:
The time complexity of the above algorithm is O(N∗logN), where ‘N’ is the total number of appointments. Though we are iterating the intervals only once, our algorithm will take O(N * logN) since we need to sort them in the beginning.

# Space complexity:
The space complexity of the above algorithm will be O(N), which we need for sorting. For Java, Arrays.sort() uses Timsort, which needs O(N) space.
