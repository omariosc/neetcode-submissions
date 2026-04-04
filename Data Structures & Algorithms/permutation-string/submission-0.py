class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        r = 0
        while r < len(s2):
            tmp = counter.copy()
            
            while counter[s2[r]] and counter[s2[r]] > 0:
                counter[s2[r]] -= 1
                r += 1
            
            flag = 1
            for value in counter.values():
                if value != 0:
                    flag = 0
                    break
            
            if flag: 
                return True
            else: 
                counter = tmp.copy()

            r += 1
        return False



        
        # counterS1, counterS2 = Counter(s1), Counter(s2)
        # difference = counterS2 - counterS1
        # for value in difference.values():
        #     if value < 0:
        #         return False
        # return True