class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = collections.defaultdict(list)
        mapping = [-1] * len(nums1)
        for j, n in enumerate(nums2):
            positions[n] = j
        for i, n in enumerate(nums1):
            mapping[i] = positions[n]
        return mapping