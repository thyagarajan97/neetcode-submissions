class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        if len(intervals) == 0:
            return [newInterval]
        ret_list = []
        inserted = False
        for start, end in intervals:
            if (not inserted) and (new_start <= start):
                ret_list.append([new_start, new_end])
                inserted = True
            ret_list.append([start, end])
        #end for
        if inserted == False:
            #Need to insert in end
            ret_list.append(newInterval)
        #end if
        finish_list = []
        finish_list.append([ret_list[0][0], ret_list[0][1]])
        #Merging the overlapping elements if any
        for start, end in ret_list:
            if finish_list[-1][1] >= start:
                finish_list[-1][1] = max(end, finish_list[-1][1])
            else:
                finish_list.append([start, end])
            #end if
        #end for
        return finish_list
    #end def