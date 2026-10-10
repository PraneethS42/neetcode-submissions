class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # trying nlogn solution first
        # add each to hash map of its sorted
        m = {}
        for word in strs:
            s = "".join(sorted(word))
            if s not in m:
                m[s] = [word]
            else:
                m[s] += [word]
        
        output = []
        for anagram in m:
            s = []
            for word in m[anagram]:
                s.append(word)
            output.append(s)

        return output