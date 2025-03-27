counter = 0
for _ in range(int(input())):
    p, v, t = input().split(" ")
    p, v, t = int(p), int(v), int(t)
    if (p + v + t) >= 2:
        counter += 1

print(counter)
