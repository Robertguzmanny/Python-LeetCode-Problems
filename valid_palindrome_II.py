class Solution:
    def validPalindrome(self, s):
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        odd_counts = sum(1 for count in char_count.values() if count % 2 !=0)

        return odd_counts <= 1

test = Solution()

s = "aba"
print(test.validPalindrome(s))

s = "aaaab"
print(test.validPalindrome(s))