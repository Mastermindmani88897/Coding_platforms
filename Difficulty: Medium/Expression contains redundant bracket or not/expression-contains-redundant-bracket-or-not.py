class Solution:
    def checkRedundancy(self, s):
        stack=[]
        ops=set("+-*/")
        
        for ch in s:
            if ch==')':
                has_op=False
                while stack and stack[-1]!='(':
                    if stack[-1] in ops:
                        has_op=True
                    stack.pop()
                stack.pop()
                if not has_op:
                    return True
            else:
                stack.append(ch)
        return False
