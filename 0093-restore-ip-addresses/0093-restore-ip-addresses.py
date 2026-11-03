class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        result = []

        def backtrack(index, path):

            if len(path) == 4:
                if index == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):

                if index + length > len(s):
                    break

                segment = s[index:index + length]

                if len(segment) > 1 and segment[0] == '0':
                    continue

                if int(segment) > 255:
                    continue

                backtrack(index + length, path + [segment])

        if 4 <= len(s) <= 12:
            backtrack(0, [])

        return result