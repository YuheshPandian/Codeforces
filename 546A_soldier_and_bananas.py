price,money,count = input().split() 
price,money,count = int(price), int(money), int(count)

def calculate_money_needed(price,count):
	initial_price = price
	for i in range(2,count+1):
		price = price + i*initial_price
	return price 


cost = calculate_money_needed(price,count)
if (cost-money)>=0:
	print(cost-money)
else:
	print(0)


