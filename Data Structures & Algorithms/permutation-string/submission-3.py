class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Thoughts - If the current character isn't in s1, then reset the window
        # Rn just make a hash map for the word we want
        seen = {}
        word = {}
        for ch in s1:
            word[ch] = 1 + word.get(ch,0)
        
        l = 0
        for r in range(len(s2)):
            ch = s2[r]
            if ch not in word:
                l = r+1
                seen = {}
            else:
                seen[ch] = 1 + seen.get(ch, 0)
                while seen[ch] > word[ch]:
                    seen[s2[l]] -= 1
                    l+=1

            # Valid window found
            if (r-l+1) == len(s1):
                return True

        return False
