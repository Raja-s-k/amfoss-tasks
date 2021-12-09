a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
c=int(b[0])
d=0

for i in b:
    i=int(i)
    if c < i:
        d+=1
    c=i

print(d)

a.close()
