year = int(input())
beautiful_year = year

while True:
    beautiful_year += 1
    if beautiful_year > year and len(set(str(beautiful_year))) == 4:
        break
print(beautiful_year)
