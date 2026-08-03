import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heapq.heapify(arr)
    return heapq.heappop(arr)

def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    res = []
    heapq.heapify(arr)
    for i in range(4):
        res.append(heapq.heappop(arr))
    return res

def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    res = []
    heapq.heapify(arr)
    for i in range(2):
        res.append(heapq.heappop(arr))
    res.reverse()
    return res
# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

