# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


def merge(intervals):
    res = []
    intervals.sort(key=lambda i:i[0])

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res

intervals = [[1,3],[1,5],[6,7]]
print(merge(intervals))