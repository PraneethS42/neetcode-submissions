class Solution:
    def isPalindrome(self, s: str) -> bool:
        # If it was all lowercause and not alphanum, can reverse and check
        # Instead use two pointers
        lp = 0
        rp = len(s)-1

        while lp < rp:
            while not s[lp].isalnum() and lp < rp:
                lp+=1
            while not s[rp].isalnum() and lp < rp:
                rp-=1
            if lp < rp and s[lp].lower() != s[rp].lower():
                return False
            lp+=1
            rp-=1
        return True

