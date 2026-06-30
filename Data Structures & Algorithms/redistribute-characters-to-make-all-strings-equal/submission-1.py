from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter.update(word)

        n = len(words)
        for freq in counter.values():
            if freq % n != 0:
                return False

        return True        