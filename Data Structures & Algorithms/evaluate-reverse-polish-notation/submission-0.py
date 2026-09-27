class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        for c in tokens:
            if c is '+':
                a,b=stack.pop(),stack.pop()
                stack.append(a+b)
            elif c is '-':
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif c is '*':
                a,b=stack.pop(),stack.pop()
                stack.append(a*b)
            elif c is '/':
                a,b=stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(c))
        return stack[0]


        