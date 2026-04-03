class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2set: dict[int, int] = {}
        for i in range(len(nums2)):
            nums2set[nums2[i]] = i
        
        res = []
        print(nums2set)
        for i in range(len(nums1)):
            if nums1[i] in nums2set:
                res.append(nums2set[nums1[i]])
        return res

