num1 = input()
num2 = input()

answer_number = ""
for position, digit in enumerate(list(num1)):
    if num1[position] == num2[position]:
        answer_number = answer_number + "0"
    else:
        answer_number = answer_number + "1"

print(answer_number)
