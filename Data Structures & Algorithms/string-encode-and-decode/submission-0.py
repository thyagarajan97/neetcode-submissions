class Solution:

    def encode(self, strs: List[str]) -> str:
        #At the begining of every-string encode with the length of the str
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the delimiter '#'
            j = s.find('#', i)
            length = int(s[i:j])
            # Move past '#' and slice the exact string length
            i = j + 1
            result.append(s[i:i + length])
            i += length
        return result