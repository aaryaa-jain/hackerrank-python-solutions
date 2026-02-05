# Problem: Set Difference Operation
# Platform: HackerRank

count_a = int(input())
set_a = set(map(int, input().split()))

count_b = int(input())
set_b = set(map(int, input().split()))

difference_set = set_a.difference(set_b)
print(len(difference_set))
