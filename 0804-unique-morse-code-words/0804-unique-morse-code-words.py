class Solution:

    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res=set()

        for w in words:

            code=""

            for ch in w:

                code+=morse[ord(ch)-ord('a')]

            res.add(code)

        return len(res)