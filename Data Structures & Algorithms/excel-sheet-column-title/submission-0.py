class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = ""
        while columnNumber > 0:
            columnNumber -= 1
            column += chr(ord('A') + (columnNumber % 26))
            columnNumber //= 26
        return column[::-1]