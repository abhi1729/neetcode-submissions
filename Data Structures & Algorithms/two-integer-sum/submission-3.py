class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap = {}
        for i in range(len(nums)):
            smap[nums[i]] = i
        print(smap)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in smap and i != smap[complement]:
                return [i,smap[complement]]
            

        