import collections
class Solution:
    # Method to sort characters of 's' according to the custom order defined in 'order'.
    def customSortString(self, order: str, s: str) -> str:
        # Count the occurrences of each character in 's' using a Counter, which is a specialized dictionary.
        s_counts = collections.Counter(s)

        # Initialize an empty list to build the sorted string.
        string_builder = []

        # Iterate over each character in the custom order 'order'.
        for char in order:
            # If the current character is present in 's' (checked via 's_counts'),
            if char in s_counts:
                # Extend 'string_builder' by the current character, repeated according to its count in 's'.
                string_builder.extend([char] * s_counts[char])
                # Remove the current character from 's_counts' to avoid re-adding it later.
                del s_counts[char]

        # Iterate over the remaining characters in 's_counts' that were not in 'order'.
        for char, count in s_counts.items():
            # Extend 'string_builder' by each of these characters, repeated according to their count.
            string_builder.extend([char] * count)

        # Join the characters in 'string_builder' into a single string and return it.
        return "".join(string_builder)

test = Solution()
order = "cba"
s = "abcd"
print(test.customSortString(order, s)) # "cbad"