class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        a=0
        u=[]
        n=0
        for l in s:
            if l in u:
                n=len(u)
                if n>a:a=n
                u=u[u.index(l)+1:]
            u.append(l)
        n=len(u)
        if n>a:return n
        return a
        
print(Solution().lengthOfLongestSubstring("aukysdfgyawuendyuewfeyyfwl"))
