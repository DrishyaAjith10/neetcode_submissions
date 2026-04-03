class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = {}
        for i in strs:
            s=tuple(sorted(i))
            if s not in prevMap:
                prevMap[s]=[]
            prevMap[s].append(i)
        return list(prevMap.values())

