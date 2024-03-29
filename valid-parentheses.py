class Solution:
    def isValid(self, s):
        stack = []
        bracket_pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_pairs.values():
                stack.append(char)
            elif char in bracket_pairs:
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False

        return not stack

test = Solution()
s = "()"
print(test.isValid(s))