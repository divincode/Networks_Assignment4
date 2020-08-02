f=open("bgp-routing-table.txt","r")
m=open("ans2.txt","w")
pre=set()
A=set()
i=0
for line in f:
    field=line.split("|")
    test=field[5].startswith(("103.21.124","103.21.125","103.21.126","103.21.127"))
    i+=1
    if test:
        print(str(i)+",prefix="+field[5]+"  AS path="+field[6]+"\n")
        m.write(str(i)+",prefix="+field[5]+"  AS path="+field[6]+"\n")
f.close()
m.close()