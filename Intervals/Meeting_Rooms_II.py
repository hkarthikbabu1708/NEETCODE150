# Given an array of meeting time interval objects consisting of start and end times
# [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
# find the minimum number of days required to schedule all meetings without any conflicts.

import heapq
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda i:i[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)

# intervals = [(0,40),(5,10),(15,20)]
intervals = [(4,9)]
print(minMeetingRooms(intervals))