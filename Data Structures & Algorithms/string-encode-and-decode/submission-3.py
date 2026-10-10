class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        for word in strs:
            e += str(len(word)) + '!' + word
        return e
        
    def decode(self, s: str) -> List[str]:
        words = []
        index = 0
        while index < len(s):
            num = ""
            while s[index] != "!":
                num += s[index]
                index += 1
            num = int(num)
            words.append(s[index+1:index+1+num])
            index = index + 1 + num
        return words

        # Need to read the number then the ! and then the word
