
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        return [item[0] for item in heapq.nlargest(n = k, iterable = freq_dict.items(), key = lambda x: x[1])]