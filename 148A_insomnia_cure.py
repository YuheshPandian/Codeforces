k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damaged_dragons = set()

if k == 1 or l == 1 or m == 1 or n == 1:
    print(d)
else:
    for x in [k, l, m, n]:
        damaged_dragons.update(range(x, d + 1, x))
    print(len(damaged_dragons))
