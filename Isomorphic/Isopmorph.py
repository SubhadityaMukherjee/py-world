n = int(input())
def isoset(x):
    l= set()
    for a in x:
        if x.count(a)>1:
            p= list()
            for b in range(len(x)):
                if a==x[b]:
                    p.append(b+1)
            if len(p)>0:
                l.add(tuple(p))
    if len(l)>1:
        return(l)
    else:
        return('n')
    
fno = input().rstrip()
f = 0
l=[]
for a in range(1,n):
    x = input().rstrip()
    if len(fno)==len(x) and isoset(fno)!='n' and isoset(x)!='n' and isoset(fno)==isoset(x):
        l.append(x)
        f=1
if f == 0:
    print('No isomorphic')
    exit()
else:
    print(fno)
    for a in l:
        print(a)
