asc=[0,0,0,0]
a=["2222q","e2222","n2nn","hh222"]
result=0
for i in range(len(a)):
	for j in a[i]:
		asc[i]+=ord(j)
	print("asc["+str(i)+"]=",asc[i])
	result+=asc[i]

print(round(result/4))