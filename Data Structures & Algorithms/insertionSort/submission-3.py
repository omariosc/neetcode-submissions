class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        for i in range(len(pairs)):
            curr = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > curr.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = curr
            res.append(pairs[:])  # snapshot

        return res