from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append(tuple([value, timestamp]))

    def get(self, key: str, timestamp: int) -> str:
        if not self.hash_map.get(key):
            return ""
        l1 = self.hash_map[key]
        #l = l1[0][1]
        l = 0
        #r = l1[len(l1)-1][1]
        r = len(l1)-1
        ret_val = ""
        target = timestamp
        #print(l1)
        while l<=r:
            mid = (l+r)//2
            #print(f' l= {l}, r = {r}, mid = {mid}')
            if l1[mid][1] == target:
                #print('found target')
                return l1[mid][0]
            
            if l1[mid][1] > target:
                r= mid-1
            else:
                l=mid+1
                ret_val = l1[mid][0]
            #end if
        #end while
        #print(f'Ret_val: {ret_val}')
        return ret_val