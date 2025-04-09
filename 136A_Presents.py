n = int(input())

friends = list(map(lambda x: int(x), input().rstrip().split()))

answer = []

for value in sorted(friends):
    answer.insert(value, str(friends.index(value) + 1))

print(" ".join(answer))
