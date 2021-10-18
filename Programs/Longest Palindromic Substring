def expand(s,Left,Right):
    L,R=Left,Right
    while L>=0 and R<len(s) and s[L]==s[R]:
        L=L-1
        R=R+1
    return R-L-1
s=input()
if len(s)<1:
    print("''")
a,b=0,0
for i in range(0,len(s)):
    l1=expand(s,i,i)
    l2=expand(s,i,i+1)
    l=max(l1,l2)
    if l>b-a:
        a=i-((l-1)//2)
        b=i+(l//2)
print(s[a:b+1])
