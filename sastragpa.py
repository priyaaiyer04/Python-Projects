c=[]
p=[]
s=0
n=int(input("enter number of courses"))
for d in range(n):
    i=int(input("credits"))
    j=int(input("grade"))
    c.append(i)
    p.append(j)
for i in range(n):
    s+=p[i]*c[i]
print(s/sum(c))