class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in visited :
                visited[char]+=1
            else :
                visited[char] = 1
        for char in t :
            if char in visited:
                visited[char]-=1
            else:
                return False
        for keys in visited:
            if visited[keys] != 0 :
                return False
        return True

        