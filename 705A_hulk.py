phrase1 = "I hate it"
phrase2 = "I love it"

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print("I love", end=" ")
    else:
        print("I hate", end=" ")
    if n > 1 and i != n:
        print("that", end=" ")
print("it")
