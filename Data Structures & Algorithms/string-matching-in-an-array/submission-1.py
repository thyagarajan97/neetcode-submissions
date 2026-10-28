class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret_set = set()
        for i in range(len(words)):
            for j in range(0, len(words)):
                if words[i] in words[j] and words[i] not in ret_set and i != j:
                    ret_set.add(words[i])
                #end if
            #end for
        #end for
        return list(ret_set)
            