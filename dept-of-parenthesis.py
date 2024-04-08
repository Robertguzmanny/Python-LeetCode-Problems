class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0

        for c in s:
            if c == "(":
                count += 1

            elif c == ")":
                count -= 1
            res = max(res, count)

        return res

test = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(test.maxDepth(s)) # 3