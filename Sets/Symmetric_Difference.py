# Problem: Symmetric Difference
# Platform: HackerRank

count_a = int(input())
set_a = set(map(int, input().split()))

count_b = int(input())
set_b = set(map(int, input().split()))

symmetric_diff = sorted(set_a ^ set_b)

for value in symmetric_diff:
    print(value)
