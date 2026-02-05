# Problem: itertools.combinations_with_replacement()
# Platform: HackerRank

from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

chars = sorted(s)

for comb in combinations_with_replacement(chars, k):
    print(''.join(comb))
