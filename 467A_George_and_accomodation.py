n = int(input())

count = 0
for _ in range(n):
    p, q = input().split()
    p, q = int(p), int(q)
    if p < (q - 1):
        count += 1
print(count)
