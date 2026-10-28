class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret_set = list()
        for i in range(len(words)):
            for j in range(0, len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    ret_set.append(words[i])
                    break
                #end if
            #end for
        #end for
        return ret_set
            