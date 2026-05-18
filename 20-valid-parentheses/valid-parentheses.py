class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for i in s:

            # opening brackets
            if i not in pairs:
                stack.append(i)

            # closing brackets
            else:
                if stack == []:
                    return False

                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False

        return stack == []