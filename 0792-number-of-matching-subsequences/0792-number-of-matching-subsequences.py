
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        buckets = defaultdict(list)

        for word in words:
            buckets[word[0]].append(iter(word[1:]))

        ans = 0

        for ch in s:
            current = buckets[ch]
            buckets[ch] = []

            for word in current:
                nxt = next(word, None)

                if nxt is None:
                    ans += 1
                else:
                    buckets[nxt].append(word)

        return ans
