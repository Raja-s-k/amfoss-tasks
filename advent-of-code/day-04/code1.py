a=open("inputdata.txt","r")
b=a.read()
b=b.splitlines()
c=[]
c.append(b[0:b.index("")])
c1=c[0][0].split(",")
c=[]
d=0

for i in c1:
    i=int(i)
    c.append(i)

print(c)

for i in b:
    d+=1
    if i=="" and d==2:
        print("\n")
    else:
        print(i)
