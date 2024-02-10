class Solution:
    def subsets(self, nums):
        nums.sort()
        result = [[]]

        for num in nums:
            result += [i + [num] for i in result]

        return result
test = Solution()
nums = [1,2,3,4]

print(test.subsets(nums))

