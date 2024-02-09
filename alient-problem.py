

def is_alien_sorted(words, order):
    # Create a dictionary that maps each letter in the alien language to its index in the 'order' string.
    # This tells us the lexicographical precedence of each letter.
    alien_dict = {letter: index for index, letter in enumerate(order)}

    # Helper function to transform a word into a list of indices according to the alien language.
    # Each letter of the word is replaced by its corresponding index from the alien language order.
    def transform(word):
        return [alien_dict[letter] for letter in word]

    # Iterate over the 'words' list, checking each word against the next one.
    for i in range(len(words) - 1):  # We go up to the second-to-last word.
        word1 = transform(words[i])  # Transform the current word into alien indices.
        word2 = transform(words[i + 1])  # Transform the next word into alien indices.

        # Compare the two transformed words. If the first is greater than the second,
        # they are not sorted correctly according to the alien dictionary, so we return False.
        if word1 > word2:
            return False

    # If we've gone through all the words without finding any out of order,
    # it means they are sorted correctly, so we return True.
    return True


# Example usage:
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(
    is_alien_sorted(words, order))  # Should return True because 'hello' comes before 'leetcode' in the alien language.

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"
print(is_alien_sorted(words,
                      order))  # Should return False because 'word' does not come before 'world' in the alien language.

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
print(is_alien_sorted(words,
                      order))  # Should return False because 'apple' should not come before 'app' in any lexicographical order when the second word is a prefix of the first.
