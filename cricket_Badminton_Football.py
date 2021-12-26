
tn = []
T = int(input("Enter Number of Students : "))  
for i in range(T):
	names = input("Enter Their Names : ")
	tn.append(names) 
print("Students Names : ",tn)


cn=[]
C = int(input("Enter Number of Student Who Play Cricket : "))   
for i in range(C):
	names0 = input("Enter Their Names : ")
	cn.append(names0)
	

bn=[]
B = int(input("Enter Number of Student Who Play Badminton : "))
for i in range(B):
	names1 = input("Enter Their Names : ")
	bn.append(names1)
	
	
fn=[]
F = int(input("Enter Number of Student Who Play Football "))   
for i in range(F):
	names1 = input("Enter Their Names ")
	fn.append(names1)


def CnB():
	groupCB=[]
	for c in cn:
		for b in bn:
			if c == b:
				groupCB.append(c)
	print("List of student who play both cricket and badminton : ",groupCB)
	print()


def CnbN():
	groupCbad =[]
	for c in cn:
		if c not in bn:
			groupCbad.append(c)
	for b in bn:
		if b not in cn:
			groupCbad.append(b)
	print("list of student who play either cricket or badminton but not both : ",groupCbad)
	print()


def nCB():
	grpNcNd=[]
	for t in tn:
		if t not in cn and bn:
			grpNcNd.append(t)
	print("List of student who play neither cricket nor badminton :",grpNcNd)
	print()


def CnF():
	grpCFnB=[]
	for t in tn:
		if t not in bn:
			grpCFnB.append(t)
	print("List of student who play cricket and football but not badminton : ",grpCFnB)


CnB()
CnbN()
nCB()
CnF()





