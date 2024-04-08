class Solution:
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, res = [], 0

        for c in s:
            if c == "(":
                stack.append(c)
                res = max(res, len(stack))
            elif c == ")":
                stack.pop()

        return res

test = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(test.maxDepth(s)) # 3