from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
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



class Solution:
  def addBoldTag(s: str, words: List[str]) -> str:
    n = len(s)
    ans = []
    # bold[i] := True if s[i] should be bolded
    bold = [0] * n

    boldEnd = -1  # s[i:boldEnd] should be bolded
    for i in range(n):
      for word in words:
        if s[i:].startswith(word):
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









        





