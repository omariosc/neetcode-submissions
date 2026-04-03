class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + '#' + string
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        length = ""
        c = 0
        while c < len(s):
            while s[c] != "#":
                length += s[c]
                c += 1
            c += 1
            decoded_string.append(s[c:c+int(length)])
            c += int(length)
            length = ""
            
        return decoded_string