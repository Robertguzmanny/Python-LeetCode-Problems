from typing import List

class Solution:
    # Define a class Solution with a method subarraySum to find the number of subarrays whose sum equals k.
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables to store the result, prefix sum, and a dictionary to store prefix sums and their frequencies.
        res = 0  # Counter for the number of subarrays with sum equal to k.
        presum = 0  # Prefix sum initialized to 0.
        dict1 = {0: 1}  # Dictionary to store prefix sums and their frequencies, initialized with 0: 1.

        # Iterate through the elements of the input list.
        for i in nums:
            # Update the prefix sum by adding the current element.
            presum = presum + i

            # If the difference between the current prefix sum and k exists in the dictionary,
            # increment the result by the frequency of that difference.
            if (presum - k) in dict1:
                res = res + dict1[presum - k]

            # If the current prefix sum is not in the dictionary, add it with a frequency of 1.
            if presum not in dict1:
                dict1[presum] = 1

            # If the current prefix sum is already in the dictionary, increment its frequency.
            else:
                dict1[presum] = dict1[presum] + 1

        # Return the final result.
        return res

test = Solution()
nums = [1,1,1]
k = 2
print(test.subarraySum(nums,k))
