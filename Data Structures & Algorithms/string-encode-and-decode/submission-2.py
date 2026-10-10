class Solution:
    # If you state the length of the word and the delimiter #, then won't misscan
    def encode(self, strs: List[str]) -> str:
        o = ""
        for word in strs:
            o += str(len(word)) + "#" + word
        return o

    def decode(self, s: str) -> List[str]:
        words = []
        # ACCOUNT FOR DOUBLE DIGIT NUMS - CHANGE
        i = 0 # Store externally, so can modify without constraint of being the looping var
        while i < len(s):
            # First get the length of the unscrambled word
            num = ""
            j = i
            while s[j].isnumeric():
                num += s[j]
                j += 1
            strlen = int(num)

            words.append(s[j+1 : j+1+strlen])
            i = j+1+strlen
        return words

