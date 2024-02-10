import random

class Solution:
    def findKthLargest(self, nums, k):
        return self.quicksort(nums, len(nums) - k, 0, len(nums) - 1);

    def quicksort(self, nums, k, a, b):
        # partition
        r = random.randint(a, b)
        nums[r], nums[b] = nums[b], nums[r]
        p = b  # set pivot to rightmost element
        i, j = a, b - 1
        while (i <= j):
            if (nums[i] < nums[p]):
                i += 1
            else:
                if (nums[j] > nums[p]):
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1;
                    j -= 1;

        nums[i], nums[p] = nums[p], nums[i]
        if (i > k):
            return self.quicksort(nums, k, a, i - 1);
        elif (i < k):
            return self.quicksort(nums, k, i + 1, b);
        else:
            return nums[k]

test = Solution()

nums = [3,2,1,5,6,4]
k = 2

print(test.findKthLargest(nums, k))