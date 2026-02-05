# Problem: Set Symmetric Difference Operation
# Platform: HackerRank

count_a = int(input())
set_a = set(map(int, input().split()))

count_b = int(input())
set_b = set(map(int, input().split()))

sym_difference = set_a.symmetric_difference(set_b)
print(len(sym_difference))
