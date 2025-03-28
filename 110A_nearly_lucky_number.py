number = input()

four_count = 0
seven_count = 0

for digit in number:
    if digit == "4":
        four_count += 1
    elif digit == "7":
        seven_count += 1

total_lucky_digits = four_count + seven_count

if total_lucky_digits == 4 or total_lucky_digits == 7:
    print("YES")
else:
    print("NO")
