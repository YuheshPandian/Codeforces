n = int(input())

prev_magnet: str = ""
curr_magnet: str = ""
groups: int = 1

for i in range(n - 1):
    if i == 0:
        prev_magnet = input()
        curr_magnet = input()
    else:
        prev_magnet = curr_magnet
        curr_magnet = input()
    if curr_magnet[0] != prev_magnet[-1]:
        pass
    else:
        groups += 1


print(groups)
