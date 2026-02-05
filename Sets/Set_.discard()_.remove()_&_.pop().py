# Problem: Set .discard(), .remove() & .pop()
# Platform: HackerRank

n = int(input())
numbers = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    command = input().split()

    if command[0] == "pop":
        numbers.pop()

    elif command[0] == "remove":
        numbers.remove(int(command[1]))

    elif command[0] == "discard":
        numbers.discard(int(command[1]))

print(sum(numbers))
