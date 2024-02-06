class Addboldtag:
    def addingboldtag(self, string, dict):
        n = len(string)
        bold = [False] * n

        for i in range(n):
            for word in dict:
                if string.startswith(word, i):
                    for j in range(i, i + len(word)):
                        bold[j] = True

        result = []
        i = 0

        while i < n:
            if bold[i]:
                result.append("<b>")
                while i < n and bold[i]:
                    result.append(string[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(string[i])
                i += 1

        return ''.join(result)

test = Addboldtag()
string = "baseball"
dict = ["bas", "ll"]

print(test.addingboldtag(string, dict))