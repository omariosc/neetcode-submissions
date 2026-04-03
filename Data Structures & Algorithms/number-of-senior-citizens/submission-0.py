class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def getAge(detail: str) -> int:
            return int(detail[-4:-2])
        seniors = 0
        for detail in details:
            if getAge(detail) > 60:
                seniors += 1
        return seniors