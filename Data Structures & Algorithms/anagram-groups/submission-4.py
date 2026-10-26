class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash_without_ord(input):
            ret_hash = 0
            for i in input: 
                ret_hash+=hash(i)
            return ret_hash
            #end for
        from collections import defaultdict
        d1 = defaultdict(list)
        for string in strs:
            d1[hash_without_ord(string)].append(string)
        #end for
        return [l1 for l1 in d1.values()]