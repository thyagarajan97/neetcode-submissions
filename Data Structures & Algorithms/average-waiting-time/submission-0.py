class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sum_of_dist = 0
        sum_of_dist += customers[0][1]
        current_end = customers[0][0] + customers[0][1]
        for index in range(1, len(customers)):
            #print(f'{index}, Current_end-time: {current_end}')
            if customers[index][0] >= current_end:
                #no overlap
                start_time = customers[index][0]
                end_time = start_time + customers[index][1]
                current_end = customers[index][0] + customers[index][1]
                #print(f'Arrived after ending, No need of a shift: {current_end}')
            elif customers[index][0] < current_end:
                #Arrival is before the current-end, customer has to wait longer
                start_time = customers[index][0]
                end_time = current_end + customers[index][1]
                current_end = end_time
                #print(f'Arrived before ending, Shift needed: start: {start_time}, end = {end_time}')
            #end if
            wait_time = (end_time - start_time)
            #print(f'Start-time: {start_time}, end-time: {end_time}, wait_time: {wait_time}')
            sum_of_dist+=wait_time
        #end for
        return sum_of_dist/float(len(customers))
