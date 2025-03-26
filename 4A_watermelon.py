w = int(input())

for x in range(2,w,2):
	if (w-x)%2==0:
		print("YES")
		break
	else:
		continue
else:
	print("NO")