class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = {}
        mapping = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            positions[n] = i
        for j, n in enumerate(nums2):
            mapping[positions[n]] = j
        return mapping