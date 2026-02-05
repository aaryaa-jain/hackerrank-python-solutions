# Problem: Set Union Operation
# Platform: HackerRank

count_a = int(input())
set_a = set(map(int, input().split()))

count_b = int(input())
set_b = set(map(int, input().split()))

union_set = set_a.union(set_b)
print(len(union_set))
