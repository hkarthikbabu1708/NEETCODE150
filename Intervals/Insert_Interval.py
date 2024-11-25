# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval.
# intervals is initially sorted in ascending order by start_i.
# You are given another interval newInterval = [start, end].
# Insert newInterval into intervals such that intervals is still sorted in ascending order by
# start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.
# Return intervals after adding newInterval.

def insert(intervals, newInterval):
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[1:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
    res.append(newInterval)
    return  res

intervals = [[1,3],[4,6]]
newInterval = [2,5]
print(insert(intervals,newInterval))