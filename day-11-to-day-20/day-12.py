class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == "(" or symbol == "[" or symbol == "{":
                stack.append(symbol)
            elif symbol == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif symbol == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif symbol == "]":
                if not stack or stack.pop() != "[":
                   return  False
        return stack == []
        

print(Solution().isValid("(]"))