a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
c=0
d=0
f=0

for i in b:
    g=i.split(" ")
    if g[0] == "forward":
        c+=int(g[1])
        d+=f*int(g[1])
    elif g[0] == "down":
        f+=int(g[1])
    elif g[0] == "up":
        f-=int(g[1])
    else:
        pass

print(c*d)

a.close()
