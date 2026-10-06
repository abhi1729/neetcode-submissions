class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = { '(' : ')', 
        '{' : '}',
        '[' : ']'
        }
        for char in s:
            if char in valid:
                stack.append(char)
            else :
                if not stack or char != valid[stack[-1]]:
                    return False
                stack.pop()
                
        return len(stack) == 0