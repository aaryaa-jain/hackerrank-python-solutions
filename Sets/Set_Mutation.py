# Problem: Set Mutations
# Platform: HackerRank

n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    cmd = input().split()
    other = set(map(int, input().split()))

    if cmd[0] == "intersection_update":
        s.intersection_update(other)

    elif cmd[0] == "update":
        s.update(other)

    elif cmd[0] == "difference_update":
        s.difference_update(other)

    elif cmd[0] == "symmetric_difference_update":
        s.symmetric_difference_update(other)

print(sum(s))
