n=int(input())
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=[]
l1=[]
for i in range(n):
    s1=""
    for j in range(n):
        s1+=s[n-min(i,j)-1]
    l.append(s1)
for i in l:
    x=n*2-1-len(i)
    s1=i[0:x]
    s1=s1[::-1]
    s2=i+s1
    l1.append(s2)

if len(l1)%2==0:
    l1=l1+l1[::-1][1:len(l1)+1]
else:
    l1=l1+l1[0:len(l1)-1][::-1]
for i in l1:
    print(i)