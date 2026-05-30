class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k 
        list = []
        while(r<len(nums)+1):
            list.append(max(nums[l:r]))
            l+=1
            r+=1
        return list


        