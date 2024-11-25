# Given an array of intervals intervals where intervals[i] = [start_i, end_i],
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    count = 0
    max_end = float('-inf')

    intervals.sort(key=lambda i:i[1])

    for interval in intervals:
        if interval[0]  >= max_end:
            count += 1
            max_end = interval[1]

    return len(intervals) - count

# intervals = [[1,2],[2,4],[1,4]]
intervals = [[1,2],[2,4]]
print(eraseOverlapIntervals(intervals))
