# Given an integer array nums and an integer k, return the k most frequent elements within the array.
from collections import Counter
import heapq
def topKFrequent(nums,k):
    heap = []
    count = Counter(nums)

    for num, fre in count.items():
        heapq.heappush(heap, (fre,num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for fre, num in heap]

# nums = [1,2,2,3,3,3]
# k = 2
nums = [7,7]
k = 1
print(topKFrequent(nums,k))