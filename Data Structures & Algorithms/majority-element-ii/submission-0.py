class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, count1 = None, 0
        cand2, count2 = None, 0

        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1

        res = []
        if count1 > int(len(nums)/3):
            res.append(cand1)
        if count2 > int(len(nums)/3):
            res.append(cand2)
        return res