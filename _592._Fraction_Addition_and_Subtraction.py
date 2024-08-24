class Solution:
    def fractionAddition(self, e: str) -> str:
        e=e.replace("10","0")
        if e[0]!="-":e="+"+e
        e=[[i[:-2],i[-1]] for i in[e[i:i+4]for i in range(0,len(e),4)]]
        for j,i in enumerate(e): 
            for k in ["+","-",""]:
                for l in [0,1]:
                    if i[l]==k+"0":e[j][l]=k+"10"
        e=[[int(j)for j in i] for i in e]
        d=1
        for i in[i[1]for i in e]:d*=i
        n=sum([int(i[0]*d/i[1])for i in e])
        if n==0:return "0/1"
        p=[2,3,5,7]
        c=[False,False,False,False]
        while True:
            for j,i in enumerate(p):
                e = [n/i,d/i]
                if all([i == int(i) for i in e]):
                    n=int(e[0])
                    d=int(e[1])
                    continue
                c[j]=True
                if all(c):break
            if all(c):break
        return str(n)+"/"+str(d)
            
print(Solution().fractionAddition("7/3+5/2-3/10"))
