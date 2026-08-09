class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for thing in s:
            if len(stack) != 0 and thing in mapping and stack[-1] == mapping[thing]:
                stack.pop()
            else: 
                stack.append(thing)
        return len(stack) == 0