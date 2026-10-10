class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srt = defaultdict(list)
        for word in strs:
            sortedword = ''.join(sorted(word))
            srt[sortedword].append(word)
        return list(srt.values())