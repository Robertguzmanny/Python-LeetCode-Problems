class Parentheses:
    def remove(self, s: str) -> str:
        res = []

        cnt = 0
        for char in s:
            if char == '(':
                res.append(char)
                cnt += 1
            elif char == ')' and cnt > 0:
                res.append(char)
                cnt -= 1
            elif char != ')':
                res.append(char)

        filtered = []
        for char in res[::-1]:
            if char == '(' and cnt > 0:
                cnt -= 1
            else:
                filtered.append(char)

        return "".join(filtered[::-1])

test = Parentheses()
s = "lee(t(c)o)de)"
print(test.remove(s)) # ""