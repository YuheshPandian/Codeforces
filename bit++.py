x = 0
for _ in range(int(input())):
	command = input()
	if "++" in command:
		x+=1
	else:
		x-=1
 
print(x)