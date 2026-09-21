class Solution(object):
    def twoSum(self, nums, target):
        val_idx={}
        for i,num in enumerate(nums):
            if target-num in val_idx:
                return [val_idx[target-num],i]
            val_idx[num]=i


        