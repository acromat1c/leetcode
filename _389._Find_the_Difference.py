class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for letter in t:
            if letter in s:
                s=s.replace(letter,"",1)
            else:
                return letter