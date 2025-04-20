total_levels: int = int(input())

little_x_levels = input().split()[1::]
little_y_levels = input().split()[1::]

little_x_levels.extend(little_y_levels)

levels_both_can_win = set(little_x_levels)
for i in range(1, total_levels + 1):
    if str(i) not in levels_both_can_win:
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")
