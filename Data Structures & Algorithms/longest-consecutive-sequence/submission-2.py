class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s = sorted(nums)
        k = 1
        ans = 1
        for i in range(len(s)-1):
            if s[i+1] != s[i]:
                if s[i+1] == s[i] + 1:
                    k += 1
                    if ans < k:
                        ans = k
                else:
                    k = 1
        return ans 
        