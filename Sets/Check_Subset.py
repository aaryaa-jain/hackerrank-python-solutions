# Problem: Check Subset
# Platform: HackerRank

tests = int(input())

for _ in range(tests):
    size_a = int(input())
    set_a = set(map(int, input().split()))

    size_b = int(input())
    set_b = set(map(int, input().split()))

    if set_a.issubset(set_b):
        print("True")
    else:
        print("False")
