# Problem: The Captain's Room
# Platform: HackerRank

k = int(input())
numbers = list(map(int, input().split()))

counts = {}

for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for room in counts:
    if counts[room] == 1:
        print(room)
        break
