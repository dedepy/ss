x=[]
n=int(input())
l=-1
for g in range(n):
    x.append(int(input()))

for i in range(len(x)):
    a=x[i]
    for j in range(i+1,len(x)):
        b=x[j]
        for k in range(j+1,len(x)):
            c=x[k]
            if a<b+c and b<a+c and c<a+b:
                    p=a+b+c
                    s = (p / 2 * (p / 2 - a) * (p / 2 - b) * (p / 2 - c)) ** 1 / 2
                    if s>l:
                        l=s
print(l)


