class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = dict()
        
        for i in range(len(strs)):
            sorted_string = "".join(sorted(strs[i]))
            try:
                sorted_strings[sorted_string].append(i)
            except KeyError:
                sorted_strings[sorted_string] = [i]
        print(sorted_strings)
        res = []
        for string in sorted_strings:
            anagram = []
            for index in sorted_strings[string]:
                anagram.append(strs[index])
            res.append(anagram)

        return res