class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pairs = collections.defaultdict(list)
        for a, b in similarPairs:
            pairs[a].append(b)
            pairs[b].append(a)

        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and word2 not in pairs[word1]:
                return False
        
        return True