class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pairs = {}
        for a, b in similarPairs:
            pairs[a] = b
            pairs[b] = a

        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and pairs[word1] != word2:
                return False
        
        return True