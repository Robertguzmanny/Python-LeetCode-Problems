# # from typing import List
# #
# #
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i

def test_case():
    nums = [1,4,6,8,9,20]
    target = 14
    print(twoSum(nums, target))

test_case()
#from typing import List




def __addBoldTag__(words, s: str) -> str:
    n = len(s)
    ans = []
    # bold[i] := True if s[i] should be bolded
    bold = [0] * n

    boldEnd = 0  # s[i:boldEnd] should be bolded
    for i in range(n):
        for word in words:
            if s.startswith(word, i):
                boldEnd = max(boldEnd, i + len(word))

        bold[i] = boldEnd > i

    # Construct the with bold tags
    i = 0
    while i < n:
        if bold[i]:
            j = i
            while j < n and bold[j]:
                j += 1
            # s[i:j] should be bolded
            ans.append('<b>' + s[i:j] + '</b>')
            i = j
        else:
            ans.append(s[i])
            i += 1

    return ''.join(ans)

words = ["gay", "elden"]
s = "elden is a gay person"
print(__addBoldTag__(words, s))  # Output: This <b>apple</b> and <b>pear</b> are tasty


#test cases

def __test_case__():
    test_one = "eduwoo"
    test_second = "yxz123"
    test_three = "abcxyz123"
    list = ["abc","123"]

    __addBoldTag__(list, test_one)
    __addBoldTag__(list, test_second)
    __addBoldTag__(list, test_three)
    print(__addBoldTag__(list, test_one))
    print(__addBoldTag__(list, test_three))
#
#
__test_case__()
#
def countPalindromes(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
        if i < n-1 and s[i] == s[i+1]:
            dp[i][i+1] = True
    for gap in range(2, n):
        for i in range(n):
            j = i + gap
            if j >= n:
                continue
            dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += int(dp[i][j])
    return ans

def test_case():
    # s = "hi"
    # n = "hey"
    # m = "letsgo"
    list = ["ya doing", " "]
    # print(countPalindromes(s))
    # print(countPalindromes(n))
    # print(countPalindromes(m))
    print(countPalindromes(list))
test_case()


#
# class Solution:
#   def addBoldTag(s,word):
#     n = len(s)
#     ans = []
#     # bold[i] := True if s[i] should be bolded
#     bold = [0] * n
#
#     boldEnd = -1  # s[i:boldEnd] should be bolded
#     for i in range(n):
#       for word in word:
#         if s[i:].startswith(word):
#           boldEnd = max(boldEnd, i + len(word))
#       bold[i] = boldEnd > i
#
#     # Construct the with bold tags
#     i = 0
#     while i < n:
#       if bold[i]:
#         j = i
#         while j < n and bold[j]:
#           j += 1
#         # s[i:j] should be bolded
#         ans.append('<b>' + s[i:j] + '</b>')
#         i = j
#       else:
#         ans.append(s[i])
#         i += 1
#
#     return ''.join(ans)
#
#
# s = ["apple", "banana", "cherry"]
# word = "elden is a gay person"
# print(Solution.addBoldTag(s, word))

def groupAnagrams( li):
  """
  :type strs: List[str]
  :rtype: List[List[str]]
  """
  dictionary = {}
  for word in li:
    sortedWord = ''.join(sorted(word))
    # If word is not in dictionary
    if sortedWord not in dictionary:
      dictionary[sortedWord] = [word]
    # If previously it is present that means its anagram
    # was previously present
    else:
      dictionary[sortedWord] += [word]
  return [dictionary[i] for i in dictionary]

# test_SLList.py
# unittest example


def camelcase(s):
    # Write your code here
    words_count = 1

    for char in s:
        if char.isupper():
            words_count += 1
    return words_count

def test():

    string_one = "RoBeRt"
    string_two = "RoRt"
    string_thrree = "eRt"

    print(camelcase(string_one))
    print(camelcase(string_two))
    print(camelcase(string_thrree))

test()

def hackerrankInString(s):
    # Write your code here
    string = 'hackerrank'
    x = len(string)

    i = 0

    for char in s:
        if char == string[i]:
            i += 1
            if i == x:
                return "YES"

    return "NO"

def test():

    word_one = "hackerrank"
    word_two = "hello"
    word_three = "hi guys"

    print(hackerrankInString(word_one))
    print(hackerrankInString(word_two))
    print(hackerrankInString(word_three))

test()

def caesarCipher(s, k):
    # Write your code here
    a="abcdefghijklmnopqrstuvwxyz"
    A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cap_alphabets=[i for i in A]
    aplhabets=[i for i in a]
    new_s=""
    for i in s:
        if i in aplhabets:
            indx=aplhabets.index(i)
            if (indx+k) <26:
                new_s+=aplhabets[indx+k]
            else:
                m=(indx+k)-26
                while m>25:
                    m=m-26
                new_s+=aplhabets[m]
        elif i in cap_alphabets:
            indx=cap_alphabets.index(i)
            if (indx+k) <26:
                new_s+=cap_alphabets[indx+k]
            else:
                m=(indx+k)-26
                while m>25:
                    m=m-26
                new_s+=cap_alphabets[m]
        else:
            new_s+=i
    return new_s

def test():
    a = "jnfenbibh-bdejenfbh"
    b = 5
    c = "asdfghjk-lopinbfgf"
    d = 9

    print(caesarCipher(a,b))
    print(caesarCipher(a,b))
    print(caesarCipher(c,d))


test()




# def manager():
#
#     dict = {"joe":200,"jose":100,"john":60}
#     for dict in i:
#         if dict < 100:
#             return i[dict]
#
#         elif i > 100:
#             return dict[i]
#
#
#
# # dict = ["joe":200,"jose":100,"john":60]
# print(dict["joe"])
#
# manager()

def underpaid_manager_salary(current_salary, market_salary, performance_rating):
    difference = market_salary - current_salary
    performance_multiplier = performance_rating / 10
    underpaid_salary = current_salary + (difference * performance_multiplier)
    return underpaid_salary

salary = underpaid_manager_salary(50000, 70000, 8)
print(salary)

class Palindrome:
    def isPalindrome(x):
        string = str(x)
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:

                return False

            left += 1
            right -= 1

        return True


y = -121000
z = 7373

print(Palindrome.isPalindrome(y))
print(Palindrome.isPalindrome(z))

# def manager():
#     managers = {"Jose": 100, "John": 200, "Jorge": 60}
#     for i in managers:
#         if managers < 100:
#             print(i)
#         elif managers > 100:
#             print("is not underpaid")
#
#
# dict = ["joe":200,"jose":100,"john":60]
#
#
# manager()

def is_formatted_correctly(file_contents):
    open_parentheses = set(['(', '{', '['])
    close_parentheses = set([')', '}', ']'])
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for line in file_contents:
        for ch in line:
            if ch in open_parentheses:
                stack.append(ch)
            elif ch in close_parentheses:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != ch:
                    return False
    return len(stack) == 0

input_str = '''[ {company_name: (BlackRock) ticker: (BLK) stock_price: {2022-04-03: ($930) 2022-04-02: ($932)}}, {company_name: (Apple) ticker: (APPL) stock_price: {2022-04-03: ($175) 2022-04-02: ($178)}}]'''
input_lines = input_str.split('\n')
if is_formatted_correctly(input_lines):
    print("valid")
else:
    print("invalid")


def dfs(fxrate, cur, dest, cur_cost):
    # cur_cost is the calculation of total cost from src to cur currency in dfs

    # visited and max_curr are global value
    global max_curr, visited

    # Base case
    if cur in visited:
        return

    # Our answer case when src is dest
    if cur == dest:
        max_curr = max(max_curr, cur_cost)
        return

    visited.add(cur)
    # calling normal dfs
    for currency, cost in fxrate[cur]:
        if currency not in visited:
            dfs(fxrate, currency, dest, cur_cost * cost)


# I made an adjacency list of our currency with cost basically a directed graph, and implemented dfs and check at the point
# when our src is equal to dest this means there is a path so we check there whether the cost is max or not
# so for that i made max value as a global value because we need to check it every time when our src equal to dest in dfs


# fxrate = defaultdict(list)

# this is an extra input i took because we cant able to take input without knowing the no. of edges
# Your Input format should look like this
#                 3
#                 USD,JPY,109
#                 USD,GBP,0.71
#                 GBP,JPY,155
#                 USD
#                 JPY
num_of_fx = int(input())

for i in range(num_of_fx):
    # Input taken with comma seperated
    currency_1, currency_2, cost = input("input 1st current and 2nd currency and their cost").split(",")
    cost = float(cost)
    # added currency with cost in our adjacency list
    fxrate[currency_1].append((currency_2, cost))

src = input("Enter Selected currency")
dest = input("Enter target currency")

# took max_curr = -1 as default for the case if there is not any way to convert the currency
max_curr = -1
# our visited set
visited = set()
# calling dfs
dfs(fxrate, src, dest, 1)

print(max_curr)






