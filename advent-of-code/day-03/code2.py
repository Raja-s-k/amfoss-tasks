a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
b1=[]
c=13
d=12
f=0
g=0
oxygen_generator_rating=""
CO2_scrubber_rating=""

while len(b)>1:
    c-=1
    for i in b:
        if i[d-c]=="0":
            f+=1
        else:
            g+=1
    if f>g:
        for i in b:
            if i[d-c]=="0":
                b1.append(i)
                
    elif g>f:
        for i in b:
            if i[d-c]=="1":
                b1.append(i)
    else:
        for i in b:
            if i[d-c]=="1":
                b1.append(i)

    b=0
    b=b1
    b1=[]
    f=0
    g=0

for i in b:
    oxygen_generator_rating+=i

a.close()

a=open("inputdata.txt","r")
b = a.read()
b = b.splitlines()
b1=[]
c=13
d=12
f=0
g=0

while len(b)>1:
    c-=1
    for i in b:
        if i[d-c]=="0":
            f+=1
        else:
            g+=1
    if f<g:
        for i in b:
            if i[d-c]=="0":
                b1.append(i)
                
    elif g<f:
        for i in b:
            if i[d-c]=="1":
                b1.append(i)
    else:
        for i in b:
            if i[d-c]=="0":
                b1.append(i)
    b=0
    b=b1
    b1=[]
    f=0
    g=0

for i in b:
    CO2_scrubber_rating+=i

a.close()

life_support_rating=int(oxygen_generator_rating,2)*int(CO2_scrubber_rating,2)
print(life_support_rating)
