n,k=map(int,input().split())
cnt=0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            k,h,m,s=str(k),str(h),str(m),str(s)
            h=h.zfill(2)
            m=m.zfill(2)
            s=s.zfill(2)
            if k in s or k in m or k in h:
                cnt+=1

print(cnt)