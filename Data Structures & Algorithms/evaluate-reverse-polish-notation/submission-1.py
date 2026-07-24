import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                a = stack.pop() + stack.pop()
                stack.append(a)
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                d = b-a
                stack.append(d)
            elif c == "*":
                m = stack.pop() * stack.pop()
                stack.append(m)

            elif c == "/":
                a, b = stack.pop(), stack.pop()
                d = b/a
                if d < 0 :
                    d = math.ceil(d)
                else:
                    d = math.floor(d)
                stack.append(d)
            else:
                stack.append(int(c))
        return stack.pop()






        