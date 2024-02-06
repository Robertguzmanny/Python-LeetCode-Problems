from collections import defaultdict
class Anagrams:
    def group_anagrams(self, strs):

        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())

test = Anagrams()

strs = ["eat","tea","tan","ate","nat","bat"]
print(test.group_anagrams(strs))