class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] not in visited:
                visited[nums[i]] = i
            else:
                result[0] = visited[target - nums[i]]
                result[1] = i
                return result