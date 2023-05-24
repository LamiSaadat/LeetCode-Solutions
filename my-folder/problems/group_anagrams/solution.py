class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input arrays of strings
        # output nested arrays of strings

        result = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]

        return result.values()


