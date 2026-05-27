class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Hashmap = {}
        for i in range(len(numbers)):
            s = target - numbers[i]
            if s in Hashmap:
                return [Hashmap[s]+1,i+1]
            Hashmap[numbers[i]] = i