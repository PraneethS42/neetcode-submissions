class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0 
        maxlen = 0
        mp = {s[0]: 1}
        while r < len(s):
            # find max character, only max 26 keys in the dictionary anyways
            mx = 0
            for char in mp: # O(26)
                mx = max(mx, mp[char])
            if (r-l+1) - mx <= k: # is the amnt of chars that are not the most frequent char less than the amnt of replacements
                maxlen = max(maxlen, r-l+1)
                r += 1
                if r >= len(s):
                    break
                if s[r] in mp:
                    mp[s[r]] += 1
                else:
                    mp[s[r]] = 1
            else: 
                # remove the character and shift index
                mp[s[l]] -= 1
                l += 1
        return maxlen