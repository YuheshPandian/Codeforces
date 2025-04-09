n = int(input())

propotions = list(map(lambda x: int(x), input().rstrip().split()))
sum_of_propotions = sum(propotions)

print(sum_of_propotions / n)
