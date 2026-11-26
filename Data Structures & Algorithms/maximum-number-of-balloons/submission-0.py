class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t1 = 'balloon'
        from collections import Counter
        t2 = Counter(text)
        max_text = 0
        while True:
            t2['b'] -=1
            t2['a'] -=1
            t2['l'] -=2
            t2['o'] -=2
            t2['n'] -=1
            if (t2['b'] < 0) or (t2['a'] < 0) or (t2['l'] < 0) or (t2['o'] < 0) or (t2['n'] < 0):
                return max_text
            max_text+=1
        #end while

