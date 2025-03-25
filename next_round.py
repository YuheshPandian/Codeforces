n,k = input().split(" ")
n,k = int(n), int(k)

# scores list
scores = list(input().split(" "))

# this is the winners for this round count
winners_count = 0

for score in scores:
	if int(score)>=int(scores[k-1]) and int(score)>0:
		winners_count+=1

print(winners_count) # answer