user_name = input()

unique_characters = set(user_name)

if len(unique_characters)%2 ==0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")