class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        finish_list = []
        finish_list.append([intervals[0][0], intervals[0][1]])
        #Merging the overlapping elements if any
        for start, end in intervals:
            if finish_list[-1][1] >= start:
                finish_list[-1][1] = max(end, finish_list[-1][1])
            else:
                finish_list.append([start, end])
            #end if
        #end for
        return finish_list