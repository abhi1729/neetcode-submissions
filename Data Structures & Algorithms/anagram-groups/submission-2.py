class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in value:
                value[key].append(str)
            else:
                value[key] = []
                value[key].append(str)

        return list(value.values())