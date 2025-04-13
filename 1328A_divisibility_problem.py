n = int(input())

moves_list = []

for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    moves = 0
    while a % b != 0:
        a = a + 1
        moves += 1
    moves_list.append(moves)

for moves in moves_list:
    print(moves)
