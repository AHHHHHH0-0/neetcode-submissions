class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code += str(len(word)) + "#" + word
        print(code)
        return code

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            word = ""
            length = ""
            n = i
            while s[n] != "#":
                length += s[n]
                n += 1

            i += len(length) + 1
            length = int(length)

            for j in range(length):
                word += s[i + j]
            print(word)
            i += length
            result.append(word)
            word = ""

        return result

