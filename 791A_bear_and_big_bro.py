a, b = input().split()
a, b = int(a), int(b)

years = 0

while a <= b:
    a *= 3
    b *= 2
    if a <= b:
        years += 1
    else:
        years += 1
        break
print(years)
