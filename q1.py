f=open("bgp-routing-table.txt","r")

pre=set()
A=set()
for lines in f:
	field=lines.split("|")
	pre.add(field[5])
	t = field[6].split(" ")
	A.update(t)
print("prefixes="+str(len(pre)))
print("ASes="+str(len(A)))
f.close()