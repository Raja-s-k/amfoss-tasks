a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
[c,d,f,g,h,i,j,k,l,m,n,o]=[[],[],[],[],[],[],[],[],[],[],[],[]]
gamma=""
epsilon=""

for p in b:
    p=str(p)
    c.append(p[0])
    d.append(p[1])
    f.append(p[2])
    g.append(p[3])
    h.append(p[4])
    i.append(p[5])
    j.append(p[6])
    k.append(p[7])
    l.append(p[8])
    m.append(p[9])
    n.append(p[10])
    o.append(p[11])

for i in [c,d,f,g,h,i,j,k,l,m,n,o]:
    q=i.count("1")
    r=i.count("0")
    if q>r:
        gamma+="1"
        epsilon+="0"
    else:
        gamma+="0"
        epsilon+="1"


gamma=int(gamma,2)
epsilon=int(epsilon,2)

print(gamma*epsilon)

    
a.close()
