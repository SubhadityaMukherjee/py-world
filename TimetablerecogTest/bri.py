n = int(input())
a,p=0,0

arr = list()

while(n>1):
	for p in range(2):
		if(n%2==0):
			n=n/2
			a+=1
		else:
			n=(p*n+1)
			a+=1
		if(n==1):
			arr.append(n)
		else:
			continue
print(arr)
