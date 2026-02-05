# Problem: itertools.combinations()
# Platform: HackerRank

from itertools import combinations

s, k = input().split()
k = int(k)

chars = sorted(s)

for size in range(1, k + 1):
    for comb in combinations(chars, size):
        print(''.join(comb))
