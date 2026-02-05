# Problem: itertools.product()
# Platform: HackerRank

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for pair in product(a, b):
    print(pair, end=" ")
