class Solution:
    def countSeniors(self, details: List[str]) -> int:
        abv_60_cnt = 0
        for person in details:
            age = person[-4:-2]
            if int(age) > 60:
                abv_60_cnt+=1
            #end if
        #end for
        return abv_60_cnt