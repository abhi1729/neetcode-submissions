class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        value = {}
        for str in strs:
            key = self.sortedString(str)
            if key in value:
                value[key].append(str)
            else:
                value[key] = []
                value[key].append(str)

        return list(value.values())

    def sortedString(self, s) -> str:
        sorted_str = "".join(sorted(s))
        return sorted_str