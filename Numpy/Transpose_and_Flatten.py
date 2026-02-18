# Problem: Transpose and Flatten
# Platform: HackerRank

import numpy

m, n = map(int, input().split())

rows = []
for _ in range(m):
    rows.append(list(map(int, input().split())))

arr = numpy.array(rows)

print(numpy.transpose(arr))
print(arr.flatten())
