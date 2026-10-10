class Solution:
    def isPalindrome(self, s: str) -> bool:
        fp = 0
        bp = len(s)-1
        while fp < bp:
            # make sure both chars are alnum
            while not s[fp].isalnum() and fp < bp:
                fp+=1
            while not s[bp].isalnum() and fp < bp:
                bp-=1
            if fp < bp and s[fp].lower() != s[bp].lower():
                return False
            fp+=1
            bp-=1
        return True