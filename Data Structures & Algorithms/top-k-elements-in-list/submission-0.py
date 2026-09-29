class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = {}
        result = []
        for num in nums:
            if num in visited :
                visited[num]+= 1
            else :
                visited[num] =1
        sorted_pairs = sorted(
            visited.items(),
            key=lambda pair: pair[1],
            reverse=True
        )

        for i in range(k):
            result.append(sorted_pairs[i][0])
        return result
        