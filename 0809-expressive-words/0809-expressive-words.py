
class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:

        def is_stretchy(word):
            i = j = 0

            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False

                c = s[i]
                count_s = 0
                count_w = 0

                while i < len(s) and s[i] == c:
                    count_s += 1
                    i += 1

                while j < len(word) and word[j] == c:
                    count_w += 1
                    j += 1

                if count_s < count_w:
                    return False

                if count_s != count_w and count_s < 3:
                    return False

            return i == len(s) and j == len(word)

        return sum(is_stretchy(word) for word in words)
