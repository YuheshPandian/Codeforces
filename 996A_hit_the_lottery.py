denominations = [1, 5, 10, 20, 100]

amount_to_withdraw = int(input())

notes_count = 0

# Not ideal due to time constraint
# while amount_to_withdraw != 0:
#     if not (amount_to_withdraw - denominations[-1]) < 0:
#         amount_to_withdraw = amount_to_withdraw - denominations[-1]
#         notes_count += 1
#     else:
#         denominations.pop(-1)

# Optimized way
for value in reversed(denominations):
    notes_count += amount_to_withdraw // value
    amount_to_withdraw = amount_to_withdraw % value

print(notes_count)
