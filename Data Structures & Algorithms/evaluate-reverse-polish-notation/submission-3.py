class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t == '+':
                one = stack[-2]
                two = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(one + two)
            elif t == '-':
                one = stack[-2]
                two = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(one - two)
            elif t == '*':
                one = stack[-2]
                two = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(one * two)
            elif t == '/':
                one = stack[-2]
                two = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(one / two))
            else:
                stack.append(int(t))
        return stack[-1]