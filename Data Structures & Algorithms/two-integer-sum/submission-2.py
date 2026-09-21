class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict={}
        for i,num in enumerate(nums):
            if (y:=target-num) in dict:
                return[dict[y],i]
            dict[num]=i
        return []
        