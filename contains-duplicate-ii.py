class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hashset = {}
        for idx in range(len(nums)):
            if nums[idx] in hashset and abs(idx - hashset[nums[idx]]) <= k:
                return True

            hashset[nums[idx]] = idx

        return False

test = Solution()
nums = [1,2,3,1]
k = 3
print(test.containsNearbyDuplicate(nums,k))
