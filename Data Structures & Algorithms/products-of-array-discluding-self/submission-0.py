class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        pre = 1
        post = 1
        i=0
        for i in range(len(nums)-1):
            pre = pre * nums[i]
            res.append(pre)
        
        for i in range(len(nums)-1,0, -1):
            post = post * nums[i]
            res[i-1] *= post 
        return res


            

        

        

        
            

        