class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        intervalList = [intervals[0]]
        i = 1
        while i<len(intervals):
            if intervalList[-1][1] >= intervals[i][0]:
                intervalList[-1][1] = max([intervalList[-1][1], intervals[i][1]])
            else:
                intervalList.append(intervals[i])
            i+=1 
        return (intervalList)