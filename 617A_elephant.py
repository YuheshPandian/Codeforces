coordinate = int(input())

moves = [5, 4, 3, 2, 1]

steps = 0

for move in moves:
    while (coordinate - move) >= 0:
        steps += 1
        coordinate -= move

print(steps)
