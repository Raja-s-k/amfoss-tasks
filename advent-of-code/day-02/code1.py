a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
c=0
d=0

for i in b:
    f=i.split(" ")
    if f[0] == "forward":
        c+=int(f[1])
    elif f[0] == "down":
        d+=int(f[1])
    elif f[0] == "up":
        d-=int(f[1])
    else:
        pass

print(c*d)

a.close()
