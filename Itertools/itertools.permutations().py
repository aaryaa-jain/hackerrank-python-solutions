# Problem: itertools.permutations()
# Platform: HackerRank

from itertools import permutations

s, k = input().split()
k = int(k)

chars = sorted(s)

for p in permutations(chars, k):
    print(''.join(p))
