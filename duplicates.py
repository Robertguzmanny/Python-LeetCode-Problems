
# def Main_Solution(nums):
#     hash = set()
#     for n in nums:
#         if n in hash:
#             return True
#
#         hash.add(n)
#     return False
#
#
# def test():
#     nums_1 = [1,1,1,1,1,1,1,1, 2, 3, 4, 5, 2, 3, 4, 2]
#     nums_2 = [1, 2, 3, 4, 5, 2, 3, 42,]
#     nums = [1, 2, 3]
#
#
#     print(Main_Solution(nums_2))
#     print(Main_Solution(nums_1))
#     print(Main_Solution(nums))
#
#
#
# test()


# def twoSum(nums, target):
#     hashmap = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [i, hashmap[complement]]
#         hashmap[nums[i]] = i


# def test_case():
#     nums = [1, 4, 6, 8, 9, 20]
#     target = 14
#     print(twoSum(nums, target))


# test_case()

# def isAnagram(s, t):
#     return sorted(s) == sorted(t)
#
# def test():
#     s = "anagram"
#     t = "naagram"
#     print(isAnagram(s,t))
#
# test()

def areAlmostEquivalent(s, t):
    # Initialize the result array
    result = []

    # Iterate through each pair of strings
    for i in range(len(s)):
        if len(s[i]) != len(t[i]):
            result.append("NO")
        else:
            # Initialize the counts of each lowercase letter in both strings
            s_counts = [0] * 26
            t_counts = [0] * 26

            # Count the number of occurrences of each lowercase letter in both strings
            for j in range(len(s[i])):
                s_counts[ord(s[i][j]) - ord('a')] += 1
                t_counts[ord(t[i][j]) - ord('a')] += 1

            # Check if the difference between the counts of each letter is greater than 3
            for k in range(26):
                if abs(s_counts[k] - t_counts[k]) > 3:
                    result.append('NO')
                    break
            else:
                result.append('YES')

    return result

def test_case():
    s = ['aabaab', 'aaaaabby']
    t = ['abbc', 'abby']
    print(areAlmostEquivalent(s,t))
test_case()


def checkForAnagrams(word, arr):
    for x in arr:
        if (sorted(word) == sorted(x)):
            return True
    return False


def funWithAnagrams(text):
    # Write your code here
    limit = len(text)
    text.reverse()

    final_text = list(text)

    count = 0
    for i in range(0, limit):
        if text[i + 1:] and checkForAnagrams(text[i], text[i + 1:]):
            final_text.pop(i - count)
            count += 1

    return sorted(final_text)


def k_most_frequent(nums, k):
    from collections import Counter

    # Count the frequency of each element
    frequency = Counter(nums)

    # Sort elements based on their frequencies in descending order
    sorted_elements = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)

    # Return the first k elements
    return sorted_elements[:k]


# Example usage
nums = [1, 1, 1, 2, 2, 3,3,3,3,3,3]
k = 3
result = k_most_frequent(nums, k)
print(result)


def name():

    if my_name == "Diego":
        print("hey")
    else:
        print("gay")

