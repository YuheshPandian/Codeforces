total_matches = int(input())
results = input()

anton_won = 0
danik_won = 0

for result in results:
    if result == "A":
        anton_won += 1
    else:
        danik_won += 1

if anton_won > danik_won:
    print("Anton")
elif danik_won > anton_won:
    print("Danik")
else:
    print("Friendship")
