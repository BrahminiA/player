s = input()
p = list(s)
for i in range(0,len(p),2) :
    p[i],p[i+1] = p[i+1],p[i]
res = ''.join(p)
print(res)
