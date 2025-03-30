n: int = int(input())

passengers = 0
seats: list = []


for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)

    if a == 0:
        passengers = passengers + b
        seats.append(passengers)

    elif b == 0:
        passengers = passengers - a
        seats.append(passengers)
    else:
        passengers = (passengers - a) + b
        seats.append(passengers)

print(max(seats))
