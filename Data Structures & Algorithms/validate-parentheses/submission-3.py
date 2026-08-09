class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for thing in s:
            if stack and thing in mapping and stack[-1] == mapping[thing]:
                stack.pop()
            else: 
                stack.append(thing)
        return len(stack) == 0