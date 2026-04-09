class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for i in strs:
            s = tuple(sorted(i)) 
            dict[s].append(i)
        return list(dict.values())

