class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        a = ""
        for i in words:
            a += i[0]
        if a == s:return True
        return False

print(Solution().isAcronym(["alice","bob","charlie"], "abc"))