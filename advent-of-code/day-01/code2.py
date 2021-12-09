a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
c=int(b[0])+int(b[1])+int(b[2])
d=0

for i in range(1998):
    i=int(b[i])+int(b[i+1])+int(b[i+2])
    if c < i:
        d+=1
    c=i

print(d)

a.close()
