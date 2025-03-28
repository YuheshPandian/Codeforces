n, k = input().split()
n, k = int(n), int(k)

for i in range(k):
    if str(n)[-1] == "0":
        n = n // 10
    else:
        n -= 1

print(n)
