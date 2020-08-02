f=open("bgp-routing-table.txt","r")

A=set()
i=0
for line in f:
	field=line.split("|")
	test=field[5].startswith(("103.21.124","103.21.125","103.21.126","103.21.127"))
	if test:
		temp=field[6].split(" ")
		while(temp[-1] == temp[-2]):
			temp.pop()
		A.add(temp[-2])
print(A)

