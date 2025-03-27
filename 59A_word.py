word = input()

word_upper = list(word.upper())
word_lower = list(word.lower())

upper_char_count = 0
lower_char_count = 0

for char in word:
    if char in word_upper:
        upper_char_count += 1
        word_upper.pop(0)

for char in word:
    if char in word_lower:
        lower_char_count += 1
        word_upper.pop(0)


if lower_char_count >= upper_char_count:
    print(word.lower())
else:
    print(word.upper())
