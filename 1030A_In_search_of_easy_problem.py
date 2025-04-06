n = int(input())

input_list = list(map(int, input().rstrip().split()))

if sum(input_list) > 0:
    print("HARD")
else:
    print("EASY")
