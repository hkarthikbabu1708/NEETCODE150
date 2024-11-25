# Given an array of meeting time interval objects consisting of start and end times
# [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine
# if a person could add all meetings to their schedule without any conflicts.

def canAttendMeetings(intervals):
    intervals.sort(key=lambda i : i[0])
    for i in range(1, len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]
        if i1[1] > i2[0]:
            return False
    return True

# intervals = [(0,30),(5,10),(15,20)]
intervals = [(5,8),(9,15)]
print(canAttendMeetings(intervals))